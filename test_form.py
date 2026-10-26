
from pathlib import Path
import unittest

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.html = Path("index.html").read_text(
            encoding="utf-8"
        ).lower()

    def test_form(self):
        self.assertIn(
            '<form id="registrationform"', self.html
        )

    def test_student_name(self):
        self.assertIn('id="name"', self.html)

    def test_roll_number(self):
        self.assertIn('id="roll"', self.html)

    def test_email(self):
        self.assertIn('id="email"', self.html)

    def test_course(self):
        self.assertIn('id="course"', self.html)

    def test_submit(self):
        self.assertIn('type="submit"', self.html)

if __name__ == "__main__":
    unittest.main(verbosity=2)
