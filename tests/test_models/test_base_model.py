#!/usr/bin/python3
"""
    Unittest of BaseModel
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
        Test base
    """

    def setUp(self) -> None:
        """
            sets up objects for testing later
        """
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()
