#!/usr/bin/python3
"""module of 'User' class"""

from models.base_model import BaseModel
"""A class User that inherits from BaseModel"""


class User(BaseModel):
    """public class attributes for user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
