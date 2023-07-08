#!/usr/bin/python3
"""
    Unittest of City
"""
import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
        Test the class City
    """

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/city.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """
            test if City is a subclass of BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(city, "state_id")
        self.assertIs(type(city.state_id), str)
        self.assertEqual(city.state_id, "")
        self.assertTrue(city, "name")
        self.assertIs(type(city.name), str)
        self.assertEqual(city.name, "")

    if __name__ == '__main__':
        unittest.main()
