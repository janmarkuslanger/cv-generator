import unittest
from datetime import date
from cv_generator.data.work_experience import WorkExperience


class TestWorkExperience(unittest.TestCase):
    def test_work_experience_initialization(self):
        title = "Software Engineer"
        company = "Tech Company"
        start = date(2020, 1, 1)
        end = date(2021, 1, 1)
        
        work_experience = WorkExperience(title, company, start, end)
        
        self.assertEqual(work_experience.title, title)
        self.assertEqual(work_experience.company, company)
        self.assertEqual(work_experience.start, start)
        self.assertEqual(work_experience.end, end)
    
    def test_work_experience_initialization_without_end_date(self):
        title = "Software Engineer"
        company = "Tech Company"
        start = date(2020, 1, 1)
        end = None
        
        work_experience = WorkExperience(title, company, start, end)
        
        self.assertEqual(work_experience.title, title)
        self.assertEqual(work_experience.company, company)
        self.assertEqual(work_experience.start, start)
        self.assertIsNone(work_experience.end)


if __name__ == '__main__':
    unittest.main()