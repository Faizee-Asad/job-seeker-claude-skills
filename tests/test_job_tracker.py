import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.claude' / 'skills' / 'job-seeker-helper' / 'scripts' / 'job_tracker.py'
spec = importlib.util.spec_from_file_location('job_tracker', SCRIPT)
job_tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(job_tracker)


class JobTrackerTests(unittest.TestCase):
    def test_add_or_update_job(self):
        rows = []
        row = job_tracker.add_or_update_job(rows, company='ExampleCo', role='Data Analyst', status='applied')
        self.assertEqual(row['status'], 'Applied')
        self.assertEqual(len(rows), 1)
        job_tracker.add_or_update_job(rows, company='ExampleCo', role='Data Analyst', status='interviewing')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'Interviewing')

    def test_write_and_load_tracker(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'tracker.csv'
            rows = []
            job_tracker.add_or_update_job(rows, company='ExampleCo', role='Analyst')
            job_tracker.write_tracker(path, rows)
            loaded = job_tracker.load_tracker(path)
            self.assertEqual(loaded[0]['company'], 'ExampleCo')


if __name__ == '__main__':
    unittest.main()
