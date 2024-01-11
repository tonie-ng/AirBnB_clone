#!/usr/bin/python3
"""Review module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a review instance"""

        super().__init__(*args, **kwargs)
