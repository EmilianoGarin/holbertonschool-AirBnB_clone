#!/usr/bin/python3
"""
    Class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Class User inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.email = ''
            self.password = ''
            self.first_name = ''
            self.last_name = ''
