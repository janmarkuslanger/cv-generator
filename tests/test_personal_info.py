import unittest
from datetime import date
from cv_generator.data.personal_info import PersonalInfo


class TestPersonalInfo(unittest.TestCase):
    def setUp(self):
        self.firstname = "John"
        self.lastname = "Doe"
        self.birthdate = date(1990, 1, 1)
        self.birthplace = "London"
        self.title = "Software Engineer"
        self.personal_info = PersonalInfo(
            self.firstname, self.lastname, self.birthdate, self.birthplace, self.title)

    def test_firstname(self):
        self.assertEqual(self.personal_info.firstname, self.firstname)

    def test_lastname(self):
        self.assertEqual(self.personal_info.lastname, self.lastname)

    def test_birthdate(self):
        self.assertEqual(self.personal_info.birthdate, self.birthdate)

    def test_birthplace(self):
        self.assertIsNone(self.personal_info.birthplace)

    def test_title(self):
        self.assertEqual(self.personal_info.title, self.title)


if __name__ == '__main__':
    unittest.main()