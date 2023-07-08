#!/usr/bin/python3
"""
    Class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Class City inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.state_id = ''
            self.name = ''
