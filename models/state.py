#!/usr/bin/python3
"""the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """The name of the state"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
