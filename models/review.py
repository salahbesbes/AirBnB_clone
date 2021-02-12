"""
    Review modules
"""
from models.base_model import BaseModel
from uuid import UUID


class Review(BaseModel):
    place_id = "place_id"
    user_id = "place_id"
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
