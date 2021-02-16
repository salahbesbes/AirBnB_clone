#!/usr/bin/python3
"""
    State modules
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Class state inherit from Base
            Attribute:
                name (str) : name of state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
