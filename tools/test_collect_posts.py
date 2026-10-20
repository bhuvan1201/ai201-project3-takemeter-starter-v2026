import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('collector', Path(__file__).with_name('collect_posts.py'))
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def post(identifier='abc', **updates):
    value = dict(id=identifier, title='A fan visit', selftext='I watched the cars from the grandstand.\n\nA whole second paragraph.', subreddit='formula1', author='fan', is_self=True, created_utc=1600000000)
    value.update(updates)
    return value


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def options(self, *extra):
        return c.parser().parse_args(['--output', str(self.root/'labels.csv'), '--cache-dir', str(self.root/'cache'), '--delay', '1', *extra])

    def test_rejects_bad_records_and_keeps_full_text(self):
        ds = c.Dataset(self.root/'labels.csv')
        for change in ({'selftext':'[removed]'}, {'selftext':''}, {'author':'F1-Bot'}, {'is_self':False}, {'subreddit':'other'}, {'removed_by_category':'moderator'}):
            self.assertNotEqual(ds.add(post(**change), 'formula1', 'test'), 'accepted')
        original = post()
        self.assertEqual(ds.add(original, 'formula1', 'test'), 'accepted')
        self.assertEqual(ds.rows[0]['text'], original['title']+'\n\n'+original['selftext'])
        self.assertEqual(ds.rows[0]['label'], '')
        self.assertIn('reserved_for_cold_labeling', ds.rows[0]['note'])
        self.assertEqual(ds.add(post(), 'formula1', 'test'), 'duplicate')
        self.assertEqual(ds.add(post('def'), 'formula1', 'test'), 'duplicate')

    def test_import_preserves_existing_human_label(self):
        ds = c.Dataset(self.root/'labels.csv')
        ds.add(post(), 'formula1', 'test')
        ds.rows[0]['label'] = 'experience'
        ds.save()
        source = self.root/'posts.json'
        source.write_text(json.dumps([post(), post('def', title='Tyre question', selftext='Why do tyres wear unevenly?')]))
        with contextlib.redirect_stdout(io.StringIO()):
            code = c.run(self.options('--import-json', str(source), '--target', '2'))
        self.assertEqual(code, 0)
        result = c.Dataset(ds.path)
        self.assertEqual([r['label'] for r in result.rows], ['experience', ''])
        self.assertEqual(len(result.rows), 2)

    def test_resume_after_network_error(self):
        args = self.options('--target', '2')
        responses = iter([[post()], RuntimeError('connection lost')])
        def initial_fetch(params):
            item = next(responses)
            if isinstance(item, Exception): raise item
            return item
        with patch.object(c.time, 'sleep'), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(c.run(args, initial_fetch), 1)
        self.assertEqual(len(c.Dataset(args.output).rows), 1)
        # Simulate a checkpoint produced by the original collector.
        state_path = next(args.cache_dir.glob('*/state.json'))
        state = json.loads(state_path.read_text())
        state['before'] = '2020-09-13T12:26:40+00:00'
        state_path.write_text(json.dumps(state))
        def resumed_fetch(params):
            self.assertEqual(params['before'], 1600000000)
            self.assertIsInstance(params['after'], int)
            return [post('def', title='Second post', created_utc=1599999999)]
        with patch.object(c.time, 'sleep'), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(c.run(args, resumed_fetch), 0)
        self.assertEqual(len(c.Dataset(args.output).rows), 2)

    def test_reddit_listing_and_malformed_import(self):
        self.assertEqual(c.unpack({'data':{'children':[{'kind':'t3','data':post()}]}}), [post()])
        with self.assertRaises(ValueError): c.unpack({'error':'bad request'})
        with self.assertRaises(ValueError): c.unpack([{'body':'a comment'}])

    def test_bad_request_reports_server_reason_without_retry(self):
        error = c.HTTPError(c.API, 400, 'Bad Request', {}, io.BytesIO(b'invalid before date'))
        with patch.object(c, 'urlopen', side_effect=error) as request:
            with self.assertRaisesRegex(RuntimeError, 'invalid before date'):
                c.fetch({'subreddit': 'formula1'})
        self.assertEqual(request.call_count, 1)

    def test_forbidden_does_not_retry(self):
        error = c.HTTPError(c.API, 403, 'Forbidden', {}, None)
        with patch.object(c, 'urlopen', side_effect=error) as request:
            with self.assertRaisesRegex(RuntimeError, 'access blocked'):
                c.fetch({'subreddit':'formula1'})
        self.assertEqual(request.call_count, 1)


if __name__ == '__main__':
    unittest.main()
