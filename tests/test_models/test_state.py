#!/usr/bin/python3
"""
    Unittest of State
"""
import unittest
import pycodestyle
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
        Test the class State
    """

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/state.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """
            test if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
        self.assertTrue(state, "name")
        self.assertIs(type(state.name), str)
        self.assertEqual(state.name, "")

    if __name__ == '__main__':
        unittest.main()
