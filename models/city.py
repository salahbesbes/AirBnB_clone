#!/usr/bin/python3
"""
    City modules
"""
from models.base_model import BaseModel
from uuid import UUID


class City(BaseModel):
    """
        city class iherit from base
            Atrribute:
                state_id (str)
                name (str)
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
            init
        """
        super().__init__(*args, **kwargs)
