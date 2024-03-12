#!/usr/bin/python3
"""
City class to handle
state and name
City class: a subclass of BaseModel
Inheriting from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Created a class that inherits from BaseModel
    Public class attributes:
        state_id, name
    """

    state_id = ""
    name = ""
