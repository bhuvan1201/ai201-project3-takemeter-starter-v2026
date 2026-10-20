# Collecting the F1 dataset

This is a Python standard-library collector: no AI calls, API keys, or extra
packages. It imports JSON exports or reads the public Arctic Shift archive.
It uses the archive's [documented post-search endpoint](https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md).
Access from your terminal still depends on the service and your network;
a script cannot guarantee access or bypass a 403.

## Finalized Milestone 4 dataset

`labels.csv` now contains 172 reviewed, labeled posts. The 28 excluded candidates
are preserved in `notes/excluded_posts.csv`. The collection report describes the
earlier 200-candidate stage. Do not rerun the collector against this finalized
file: replaying cached pages could reintroduce excluded candidates. For any
future collection, use a separate candidate output, for example
`--output additional_candidates.csv`, and review and deduplicate before merging.

## Collect candidates automatically (original collection workflow)

From the Project 3 folder, run:

```bash
python tools/collect_posts.py --target 200
```

The default range is 2020-01-01 to 2023-01-01, so this collects historical
posts, not current F1 news. This range was chosen because our browser check
found full text in older archive records. It reads newest-first within the
range, at most 50 pages per invocation, with a two-second delay between pages.
It stops at 200 CSV rows, not 200 raw records. To choose a different period:

```bash
python tools/collect_posts.py --after 2023-01-01 --before 2026-01-01 --target 200
```

Existing CSV rows and labels are preserved. Repeating the same command resumes
from saved pages and the date cursor. Cached pages are under
`.cache/reddit_collection/` (already ignored by Git). A different date range
uses a separate cursor and still deduplicates against the same CSV.

Do not edit the CSV or run another collector against it while this command is
running. If you need more candidates after reviewing exclusions or balance,
increase `--target`; existing rows will not be reordered or truncated.

## Import a downloaded file

```bash
python tools/collect_posts.py --import-json "$HOME/Downloads/posts.json" --target 200
```

Multiple files are supported:

```bash
python tools/collect_posts.py --import-json "$HOME/Downloads/posts.json" "$HOME/Downloads/posts (1).json" --target 200
```

Supported input: a list of post objects, Arctic Shift's `data` list, or a
Reddit Listing JSON export. Comments, HTML, and search snippets are not input
formats. The first downloaded file we checked had 97 removed/deleted bodies,
two empty bodies, and one bot discussion thread, so it contributes no rows.
Importing it again cannot recover missing text.

## What is saved and what still needs your review

- `labels.csv`: title, two newlines, and the full original body in `text`;
  blank `label`; source URL and collection details in `note`.
- `labels.collection_report.json`: latest run's totals, exclusions, status,
  and any error. It is overwritten per run; existing CSV rows are retained.
- `.cache/reddit_collection/`: raw archive pages and pagination checkpoints.

The script excludes missing/removed bodies, records marked removed, non-text
or crossposted submissions, common bot/recurring threads, duplicates by ID
or normalized text, and real examples already linked in the README. It does
not judge the remaining posts' purposes or claim they meet your label balance.
The archive may contain an older version of a post; verify sources when you
review. The chronological sampling and exclusion rules are not a
random or representative sample of the subreddit.

The first 20 new rows are marked `reserved_for_cold_labeling; not_yet_labeled`,
not `cold` as if the work were already done. Label them yourself without AI,
then mark them cold. Keep your answers hidden from your independent reviewer.
All later labels also remain blank until you choose how to label them.

Manually review every candidate for English language, relevance to the four
labels, complete usable text, and any remaining recurring/news-only posts.
Check the 20–40% label balance after labeling and record three difficult cases.
Do not train on the CSV while labels are blank. Collection alone does not
complete Milestone 4.

## Status and errors

Exit 0 means the target CSV row count was reached. Exit 2 means a local import,
date range, or page budget ended below the target; the report explains which.
Exit 1 means an error or interruption; successfully collected rows are saved.
The target count describes candidates, not a completed reviewed dataset.

A 401 or 403 stops immediately. Retry later or import a browser export you can
legitimately download. Rate limits and temporary server failures get at most
three attempts. No CAPTCHA or access-control bypass is included. An exhausted
date range needs a new range; a page limit can be continued with the same command.

## Check the collector locally

```bash
python -m unittest discover -s tools -p 'test_collect_posts.py' -v
```

The tests use synthetic records only in temporary folders. They never add
fictional posts to your dataset or make network requests.
