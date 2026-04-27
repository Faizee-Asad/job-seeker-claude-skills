import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.claude' / 'skills' / 'job-seeker-helper' / 'scripts' / 'keyword_audit.py'
spec = importlib.util.spec_from_file_location('keyword_audit', SCRIPT)
keyword_audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(keyword_audit)


class KeywordAuditTests(unittest.TestCase):
    def test_detects_matched_and_missing_terms(self):
        resume = 'Data analyst with SQL and Tableau dashboarding experience.'
        job = 'Must have SQL, Python, Tableau, stakeholder communication, and A/B testing.'
        result = keyword_audit.audit(resume, job)
        matched = {item['term'] for item in result['matched_terms']}
        missing = {item['term'] for item in result['missing_terms']}
        self.assertIn('sql', matched)
        self.assertIn('tableau', matched)
        self.assertIn('python', missing)

    def test_markdown_report_contains_score(self):
        result = keyword_audit.audit('Python SQL', 'Python SQL Tableau')
        report = keyword_audit.markdown_report(result)
        self.assertIn('Coverage score', report)
        self.assertIn('ATS Keyword Audit', report)


if __name__ == '__main__':
    unittest.main()
