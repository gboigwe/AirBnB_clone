#!/usr/bin/python3
"""
Created a class User
Sub Class of BaseModel:
    To handle login like email,
    password, first_name, last_name
Class User inherits from BaseModel
"""


from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    User class created
    with public class attribute:
        email, password, first_name, last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
