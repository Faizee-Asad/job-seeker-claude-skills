import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.claude' / 'skills' / 'job-seeker-helper' / 'scripts' / 'packet_builder.py'
spec = importlib.util.spec_from_file_location('packet_builder', SCRIPT)
packet_builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packet_builder)


class PacketBuilderTests(unittest.TestCase):
    def test_build_packet_includes_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / 'cover_letter.md'
            first.write_text('# Cover Letter\nHello', encoding='utf-8')
            packet = packet_builder.build_packet([first], title='Test Packet')
            self.assertIn('Test Packet', packet)
            self.assertIn('Cover Letter', packet)
            self.assertIn('Verify all dates', packet)


if __name__ == '__main__':
    unittest.main()
