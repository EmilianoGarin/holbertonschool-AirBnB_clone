#!/usr/bin/python3
"""
    Class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
        serialization-deserialization of objects
    """
    __file_path = 'HBNB.json'
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj in __objects"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """write or overwrite the file in __file_path"""
        des = FileStorage.__objects.copy()
        for k, v in des.items():
            des[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(des))

    def reload(self):
        """reload the objects in the file in __file_path"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                ret = json.loads(f.read())
        except FileNotFoundError:
            ret = {}
        except json.decoder.JSONDecodeError:
            ret = {}
        finally:
            for k, v in ret.items():
                cls = ret[k]['__class__']
                if  'BaseModel' == cls:
                    FileStorage.__objects[k] = BaseModel(**v)
