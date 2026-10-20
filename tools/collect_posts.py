#!/usr/bin/env python3
"""Collect unlabelled Reddit text candidates; no model calls or third-party packages."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API = 'https://arctic-shift.photon-reddit.com/api/posts/search'
COLUMNS = ['text', 'label', 'note']
THREAD = re.compile(r'daily discussion|weekly discussion|trash talk thread|ask .+ anything|grand prix.*(?:discussion|debrief)|monday.*thread', re.I)
POST_ID = re.compile(r'/comments/([a-z0-9]+)', re.I)


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    temp.write_text(text, encoding='utf-8')
    os.replace(temp, path)


def save_json(path, data):
    atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def unpack(payload):
    if isinstance(payload, dict) and isinstance(payload.get('data'), list):
        records = payload['data']
    elif isinstance(payload, dict) and isinstance(payload.get('data'), dict) and 'children' in payload['data']:
        records = payload['data']['children']
    elif isinstance(payload, list):
        # Reddit thread exports are lists of Listings, not lists of posts.
        if payload and isinstance(payload[0], dict) and payload[0].get('kind') == 'Listing':
            return unpack(payload[0])
        records = payload
    else:
        raise ValueError('Expected an archive list, {data: [...]}, or Reddit Listing JSON.')
    if not isinstance(records, list):
        raise ValueError('Post records must be a list.')
    posts = []
    for item in records:
        if not isinstance(item, dict):
            raise ValueError('A post record is not an object.')
        if item.get('kind') == 't3':
            item = item.get('data', {})
        if not isinstance(item, dict) or 'title' not in item:
            raise ValueError('Record lacks a post title; comments are not supported.')
        posts.append(item)
    return posts


def rejection(post, subreddit):
    if str(post.get('subreddit', '')).casefold() != subreddit.casefold():
        return 'wrong_subreddit'
    title, body = post.get('title'), post.get('selftext')
    if not isinstance(body, str) or not body.strip():
        return 'empty_body'
    if body.strip().casefold() in ('[removed]', '[deleted]') or post.get('removed_by_category') or post.get('removed_by'):
        return 'removed_or_deleted'
    if not isinstance(title, str) or not title.strip():
        return 'empty_title'
    if not re.fullmatch('[a-z0-9]+', str(post.get('id', ''))):
        return 'missing_post_id'
    if str(post.get('author') or '').casefold() in ('automoderator', 'f1-bot') or post.get('stickied') or THREAD.search(title):
        return 'automated_or_recurring_thread'
    if post.get('is_self') is not True or post.get('crosspost_parent'):
        return 'not_original_text_post'
    # A link or image with no prose does not supply a usable body.
    prose = re.sub(r'!?\[[^\]]*\]\([^)]*\)|https?://\S+', '', body)
    if not re.search(r'[A-Za-z]{2,}', prose):
        return 'no_prose'
    return None


def fingerprint(text):
    return hashlib.sha256(' '.join(text.casefold().split()).encode()).hexdigest()


class Dataset:
    def __init__(self, path):
        self.path = path
        self.rows = []
        if path.exists():
            with path.open(encoding='utf-8-sig', newline='') as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != COLUMNS:
                    raise ValueError(f'{path} must have exactly text,label,note columns.')
                self.rows = list(reader)
            if any(set(row) != set(COLUMNS) or any(v is None for v in row.values()) for row in self.rows):
                raise ValueError('Existing CSV has malformed rows; left untouched.')
        self.ids = {m.group(1) for row in self.rows for m in POST_ID.finditer(row['note'])}
        self.hashes = {fingerprint(row['text']) for row in self.rows}
        readme = ROOT / 'README.md'
        self.examples = set(POST_ID.findall(readme.read_text())) if readme.exists() else set()

    def add(self, post, subreddit, source):
        reason = rejection(post, subreddit)
        if not reason and post['id'] in self.examples:
            reason = 'previously_discussed_readme_example'
        if reason:
            return reason
        text = post['title'] + '\n\n' + post['selftext']
        digest = fingerprint(text)
        if post['id'] in self.ids or digest in self.hashes:
            return 'duplicate'
        position = len(self.rows) + 1
        status = 'reserved_for_cold_labeling; not_yet_labeled' if position <= 20 else 'unlabelled; needs_human_review'
        url = f"https://www.reddit.com/r/{subreddit}/comments/{post['id']}/"
        note = f'{status}; source={url}; collected_via={source}'
        if post.get('created_utc') is not None:
            note += f"; created_utc={post['created_utc']}"
        self.rows.append({'text': text, 'label': '', 'note': note})
        self.ids.add(post['id'])
        self.hashes.add(digest)
        return 'accepted'

    def save(self):
        import io
        output = io.StringIO(newline='')
        writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(self.rows)
        atomic_write(self.path, output.getvalue())



def epoch_seconds(value):
    """Normalize CLI dates and old saved ISO cursors to API epoch seconds."""
    if isinstance(value, (int, float)) or str(value).isdigit():
        return int(value)
    date = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)
    return int(date.timestamp())


def fetch(params):
    request = Request(API + '?' + urlencode(params), headers={'User-Agent': 'TakeMeter-course-collector/1.0', 'Accept': 'application/json'})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                return unpack(json.load(response))
        except HTTPError as exc:
            if exc.code in (401, 403):
                raise RuntimeError(f'HTTP {exc.code}: archive access blocked. No bypass attempted. Use --import-json with a browser export, or try from an authorized network.') from exc
            if exc.code == 400:
                detail = exc.read(1000).decode('utf-8', errors='replace')
                raise RuntimeError(f'Archive rejected the request (HTTP 400): {detail}. Progress is saved.') from exc
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f'Archive returned HTTP {exc.code}; progress is saved. Retry later.') from exc
            retry = exc.headers.get('Retry-After', '')
            delay = int(retry) if retry.isdigit() else 5 * (attempt + 1)
            if delay > 60:
                raise RuntimeError(f'Server requests a {delay}s pause; stop now and retry later.') from exc
            time.sleep(delay)
        except (URLError, TimeoutError) as exc:
            if attempt == 2:
                raise RuntimeError('Archive connection failed; progress is saved. Retry later or import a JSON export.') from exc
            time.sleep(5 * (attempt + 1))


def run(args, fetcher=fetch):
    dataset = Dataset(args.output)
    initial = len(dataset.rows)
    stats = Counter()
    error = None
    status = 'target_reached' if initial >= args.target else 'incomplete'
    signature = {'subreddit': args.subreddit, 'after': args.after, 'before': args.before, 'output': str(args.output.resolve())}
    key = hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()[:16]
    cache = args.cache_dir / key
    state_path = cache / 'state.json'
    state = json.loads(state_path.read_text()) if state_path.exists() else {'before': args.before, 'pages': 0}

    def consume(posts, source):
        for post in posts:
            if len(dataset.rows) >= args.target:
                break
            stats[dataset.add(post, args.subreddit, source)] += 1
        dataset.save()

    try:
        if initial < args.target and args.import_json:
            for file in args.import_json:
                consume(unpack(json.loads(file.read_text(encoding='utf-8-sig'))), 'json_import:' + file.name)
                if len(dataset.rows) >= args.target:
                    break
            status = 'target_reached' if len(dataset.rows) >= args.target else 'import_complete_target_not_reached'
        elif initial < args.target:
            # Replay cached pages first: safe after interruption between saving CSV and cursor.
            for page in sorted(cache.glob('page_*.json')):
                consume(unpack(json.loads(page.read_text())), 'arctic_shift')
                if len(dataset.rows) >= args.target:
                    break
            for _ in range(args.max_pages):
                if len(dataset.rows) >= args.target:
                    break
                params = {'subreddit': args.subreddit, 'after': epoch_seconds(args.after), 'before': epoch_seconds(state['before']), 'sort': 'desc', 'limit': 100}
                posts = fetcher(params)
                if not posts:
                    status = 'date_range_exhausted'
                    break
                times = [int(p['created_utc']) for p in posts]
                cursor = min(times)
                if cursor >= params['before']:
                    raise RuntimeError('Pagination stopped advancing; narrow the date range rather than skipping records.')
                page_number = state['pages'] + 1
                save_json(cache / f'page_{page_number:05d}.json', posts)
                consume(posts, 'arctic_shift')
                state = {'before': cursor, 'pages': page_number}
                save_json(state_path, state)
                print(f'Page {page_number}: {len(dataset.rows)}/{args.target} candidates saved', flush=True)
                if len(dataset.rows) < args.target:
                    time.sleep(args.delay)
            else:
                status = 'page_limit_reached'
            if len(dataset.rows) >= args.target:
                status = 'target_reached'
    except (OSError, ValueError, KeyError, RuntimeError) as exc:
        error = str(exc)
        status = 'error'
    except KeyboardInterrupt:
        error = 'Interrupted by user; rerun the same command to resume.'
        status = 'interrupted'
    dataset.save()
    report = {'status': status, 'target': args.target, 'rows_before': initial, 'rows_after': len(dataset.rows), 'added_this_run': len(dataset.rows)-initial, 'outcomes_this_run': dict(stats), 'source': 'json_import' if args.import_json else API, 'date_range': {'after': args.after, 'before': args.before} if not args.import_json else None, 'error': error, 'review_required': 'Candidates only: human review must check English language, taxonomy scope, source availability, and label balance. No labels generated.'}
    save_json(args.output.with_suffix('.collection_report.json'), report)
    print(json.dumps(report, indent=2))
    return 1 if error else (0 if len(dataset.rows) >= args.target else 2)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--import-json', nargs='+', type=Path, help='Import downloaded archive or Reddit JSON instead of using the network.')
    p.add_argument('--output', type=Path, default=ROOT/'labels.csv')
    p.add_argument('--subreddit', default='formula1')
    p.add_argument('--target', type=int, default=200)
    p.add_argument('--after', default='2020-01-01', help='Archive date range start (default: 2020-01-01).')
    p.add_argument('--before', default='2023-01-01', help='Archive date range end (default: 2023-01-01; historical sample).')
    p.add_argument('--max-pages', type=int, default=50, help='Maximum API requests/pages this run, excluding limited retries.')
    p.add_argument('--delay', type=float, default=2, help='Seconds between pages (minimum 1).')
    p.add_argument('--cache-dir', type=Path, default=ROOT/'.cache'/'reddit_collection')
    return p


if __name__ == '__main__':
    cli = parser()
    options = cli.parse_args()
    if options.target < 1 or options.max_pages < 1 or options.delay < 1:
        cli.error('target and max-pages must be positive; delay must be at least 1 second.')
    try:
        start = epoch_seconds(options.after)
        end = epoch_seconds(options.before)
        if start >= end:
            cli.error('--after must be earlier than --before.')
        sys.exit(run(options))
    except (OSError, ValueError) as exc:
        cli.exit(1, f'Error: {exc}\n')
