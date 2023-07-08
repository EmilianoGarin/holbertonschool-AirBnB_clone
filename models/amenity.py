#!/usr/bin/python3
"""
    Class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Class Amenity inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.name = ''
