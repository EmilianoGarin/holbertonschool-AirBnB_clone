#!/usr/bin/python3
"""
    Unittest of User
"""
import unittest
import pycodestyle
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
        Test the class User
    """

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/user.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """
            test if User is a subclass of BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        user = User()
        self.assertTrue(isinstance(user, BaseModel))
        self.assertTrue(user, "email")
        self.assertIs(type(user.email), str)
        self.assertEqual(user.email, "")
        self.assertTrue(user, "password")
        self.assertIs(type(user.password), str)
        self.assertEqual(user.password, "")
        self.assertTrue(user, "first_name")
        self.assertIs(type(user.first_name), str)
        self.assertEqual(user.first_name, "")
        self.assertTrue(user, "last_name")
        self.assertIs(type(user.last_name), str)
        self.assertEqual(user.last_name, "")

    if __name__ == '__main__':
        unittest.main()
