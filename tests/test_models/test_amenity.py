#!/usr/bin/python3
"""
    Unittest of Amenity
"""
import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
        Test the class Amenity
    """

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/amenity.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """
            test if Amenity is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
        self.assertTrue(amenity, "name")
        self.assertIs(type(amenity.name), str)
        self.assertEqual(amenity.name, "")

    if __name__ == '__main__':
        unittest.main()
