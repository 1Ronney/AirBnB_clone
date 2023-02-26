#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
