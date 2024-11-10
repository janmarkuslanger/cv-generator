import unittest
from datetime import date
from cv_generator.data.education import Education


class TestEducation(unittest.TestCase):
    def test_education_initialization(self):
        institution = "Test University"
        degree = "Bachelor of Science"
        graduation_date = date(2023, 5, 15)
        
        education = Education(institution, degree, graduation_date)
        
        self.assertEqual(education.institution, institution)
        self.assertEqual(education.degree, degree)
        self.assertEqual(education.graduation_date, graduation_date)
    
    def test_education_initialization_without_graduation_date(self):
        institution = "Test University"
        degree = "Bachelor of Science"
        graduation_date = None
        
        education = Education(institution, degree, graduation_date)
        
        self.assertEqual(education.institution, institution)
        self.assertEqual(education.degree, degree)
        self.assertIsNone(education.graduation_date)


if __name__ == '__main__':
    unittest.main()