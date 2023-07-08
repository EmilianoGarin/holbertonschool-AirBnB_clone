#!/usr/bin/python3
"""
    Unittest of Place
"""
import unittest
import pycodestyle
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
        Test the class Place
    """

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/place.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """
            test if Place is a subclass of BaseModel
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))
        self.assertTrue(place, "city_id")
        self.assertIs(type(place.city_id), str)
        self.assertEqual(place.city_id, "")
        self.assertTrue(place, "user_id")
        self.assertIs(type(place.user_id), str)
        self.assertEqual(place.user_id, "")
        self.assertTrue(place, "name")
        self.assertIs(type(place.name), str)
        self.assertEqual(place.name, "")
        self.assertTrue(place, "description")
        self.assertIs(type(place.description), str)
        self.assertEqual(place.description, "")
        self.assertTrue(place, "number_rooms")
        self.assertIs(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(place, "number_bathrooms")
        self.assertIs(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(place, "max_guest")
        self.assertIs(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(place, "price_by_night")
        self.assertIs(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(place, "latitude")
        self.assertIs(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(place, "longitude")
        self.assertIs(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(place, "amenity_ids")
        self.assertIs(type(place.amenity_ids), list)
        self.assertEqual(place.amenity_ids, [])

    if __name__ == '__main__':
        unittest.main()
