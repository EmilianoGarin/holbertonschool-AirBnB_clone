#!/usr/bin/python3
"""
    Unittest of FileStorage
"""
import unittest
import os
import pycodestyle
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
        Test the class FileStorage
    """
    def setUp(self):
        """
            objects to test
        """
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """
            delete the file.json when finish the test
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_objects(self):
        """
            test objects
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_models_storage(self):
        """
            test if storage in init is on
        """
        self.assertIsNotNone(models.storage.all())

    def test_attributes(self):
        """
            test type and existence of all atributes
        """
        self.assertEqual(dict, type(self.storage.all()))

    def test_doc(self):
        """
            test documentation
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all(self):
        """
            test all method
        """
        self.storage.new(self.model1)
        self.storage.new(self.model2)
        all_objs = self.storage.all()
        self.assertIsNotNone(all_objs)
        self.assertIn("BaseModel." + self.model1.id, all_objs)
        self.assertIn("BaseModel." + self.model2.id, all_objs)
        self.assertIs(all_objs, self.storage._FileStorage__objects)
        self.assertEqual(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """
            test new method
        """
        self.storage.new(self.model1)
        obj_key = "BaseModel." + self.model1.id
        self.assertIn(obj_key, self.storage.all())
        self.assertEqual(self.model1, self.storage.all()[obj_key])

    def test_save_reload(self):
        """
            test save and reload method
        """
        self.storage.new(self.model1)
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        obj_key = "BaseModel." + self.model1.id
        obj_all = self.storage.all()
        obj_storage = obj_all[obj_key]
        self.assertIn(obj_key, self.storage.all())
        self.assertTrue(self.model1.__dict__ == obj_storage.__dict__)
        self.assertFalse(self.model1 is obj_storage)
        self.assertIsInstance(obj_storage, BaseModel)
        self.assertEqual(self.model1.id, obj_storage.id)

    def test_pep8(self):
        """
            Check PEP8 style
        """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/engine/file_storage.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_reload_method(self):
        """
            check if reload working
        """
        self.assertIsNotNone(FileStorage().reload)

    def test_all_subclass(self):
        """
            test all subclass of BaseModel
        """
        cls = {'BaseModel.': BaseModel, 'User.': User, 'State.': State,
               'City.': City, 'Amenity.': Amenity, 'Place.': Place,
               'Review.': Review}
        dic = {}
        stor_all = self.storage.all()
        for k, v in cls.items():
            dic[k] = v()
        for k, v in dic.items():
            self.assertIsNotNone(stor_all[k + v.id])

    if __name__ == '__main__':
        unittest.main()
