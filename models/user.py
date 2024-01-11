#!/usr/bin/python3
"""User Model."""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes a User class based in the BaseModel"""

        super().__init__(*args, **kwargs)
