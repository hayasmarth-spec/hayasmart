import unittest
from main import process_smart_command

class TestHayaSmart(unittest.TestCase):
    def test_command_processing(self):
        self.assertEqual(process_smart_command("Turn on AC"), "Action Scheduled Successfully")

if __name__ == "__main__":
    unittest.main()
