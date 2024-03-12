#!/usr/bin/python3
"""
class Review: A subclass of BaseModel
That inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Created class Review

    Public class attribute:
        place_id, user_id, text
    """

    place_id = ""
    user_id = ""
    text = ""
