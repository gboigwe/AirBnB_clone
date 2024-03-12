#!/usr/bin/python3
"""
Amenity class that inherits from BaseModel
as a subclass from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Created a class Amenity

    It handles the public class attribute:
        name

    Handles name as string
    """

    name = ""
