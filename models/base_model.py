#!/usr/bin/python3
"""
    Class base
"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """
        Class base
    """
    def __init__(self, *args, **kwargs):
        """ initialize"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        time = datetime.fromisoformat(v)
                        setattr(self, k, time)
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """string with a description of a simple object type"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the moment it was modified"""
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """description of a simple object type"""
        des = self.__dict__.copy()
        des['created_at'] = des['created_at'].isoformat()
        des['updated_at'] = des['updated_at'].isoformat()
        des['__class__'] = self.__class__.__name__
        return des
