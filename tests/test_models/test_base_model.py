#!/usr/bin/python3
"""
    Unittest of BaseModel
"""
import unittest
import os
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
        Test the class BaseModel
    """

    def setUp(self) -> None:
        """
            sets up objects for testing later
        """
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        self.assertTrue(self.model1, "id")
        self.assertIs(type(self.model1.id), str)
        self.assertTrue(self.model1, "created_at")
        self.assertIs(type(self.model1.created_at), datetime.datetime)
        self.assertTrue(self.model1, "updated_at")
        self.assertIs(type(self.model1.updated_at), datetime.datetime)

    def test_singularity(self):
        """
            test thet ids are unique
        """
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_doc(self):
        """
            test documentation
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_str_(self):
        """
            test __str__ method
        """
        model = self.model1
        self.assertEqual(
            f"[{type(model).__name__}] ({model.id}) {model.__dict__}",
            str(model))

    def test_save(self):
        """
            test save method
        """
        update_at = self.model1.__dict__['updated_at']
        self.model1.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(self.model1.__dict__['updated_at'], update_at)

    def test_to_dict(self):
        """
            test to_dict method
        """
        dic = self.model1.to_dict()
        self.assertNotEqual(dic, self.model1.__dict__)
        self.assertEqual(dic['id'], self.model1.__dict__['id'])
        self.assertNotEqual(dic['created_at'],
                            self.model1.__dict__['created_at'])
        self.assertNotEqual(type(dic['created_at']),
                            type(self.model1.__dict__['created_at']))
        self.assertNotEqual(dic['updated_at'],
                            self.model1.__dict__['updated_at'])
        self.assertNotEqual(type(dic['updated_at']),
                            type(self.model1.__dict__['updated_at']))

    if __name__ == '__main__':
        unittest.main()
