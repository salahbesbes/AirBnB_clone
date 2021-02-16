#!/usr/bin/python3
"""
    Amenity modules
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        class Amenity inherit from base
        Attribute:
            name (str)
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            str
        """
        super().__init__(*args, **kwargs)
