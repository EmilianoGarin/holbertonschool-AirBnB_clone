#!/usr/bin/python3
"""
    Class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Class Place inherit from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.city_id = ''
            self.user_id = ''
            self.name = ''
            self.description = ''
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []