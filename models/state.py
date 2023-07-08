#!/usr/bin/python3
"""
    Class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Class State inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.name = ''
