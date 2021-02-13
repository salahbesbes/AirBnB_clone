#!/usr/bin/python3
"""
    City modules
"""
from models.base_model import BaseModel
from uuid import UUID


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
