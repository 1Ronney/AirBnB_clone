#!/usr/bin/python3
"""
Amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ intializes parent class"""
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
