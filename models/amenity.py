#!/usr/bin/python3
"""importing base_model module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """public class that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
