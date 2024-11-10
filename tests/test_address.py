import unittest
from cv_generator.data.address import Address


class TestAddress(unittest.TestCase):
    def setUp(self):
        self.address = Address("123 Main St", "Anytown", "12345", "USA")

    def test_street(self):
        self.assertEqual(self.address.street, "123 Main St")

    def test_city(self):
        self.assertEqual(self.address.city, "Anytown")

    def test_zip_code(self):
        self.assertEqual(self.address.zip_code, "12345")

    def test_country(self):
        self.assertEqual(self.address.country, "USA")


if __name__ == '__main__':
    unittest.main()