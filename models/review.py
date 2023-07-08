#!/usr/bin/python3
"""
    Class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Class Review inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.place_id = ''
            self.user_id = ''
            self.text = ''
