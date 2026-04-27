import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.claude' / 'skills' / 'job-seeker-helper' / 'scripts' / 'validate_skill.py'
spec = importlib.util.spec_from_file_location('validate_skill', SCRIPT)
validate_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_skill)


class ValidateSkillTests(unittest.TestCase):
    def test_validate_repo_skills(self):
        root = Path(__file__).resolve().parents[1] / '.claude' / 'skills'
        ok, errors = validate_skill.validate(root)
        self.assertTrue(ok, errors)

    def test_parse_frontmatter(self):
        text = '---\nname: test\ndescription: Test skill\n---\nBody'
        meta = validate_skill.parse_frontmatter(text)
        self.assertEqual(meta['name'], 'test')


if __name__ == '__main__':
    unittest.main()
