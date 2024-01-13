#!/usr/bin/python3
"""
Defines a base class.
"""

from uuid import uuid4
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    A base model class that provides common
    attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        val = datetime.strptime(val, time_format)
                    if key == 'updated_at':
                        val = datetime.strptime(val, time_format)
                    setattr(self, key, val)

    def save(self):
        """updates the `updated_at` attribute."""

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of containing all elements of __dict__"""

        dictrepr = self.__dict__.copy()
        dictrepr["created_at"] = dictrepr["created_at"].isoformat()
        dictrepr["updated_at"] = dictrepr["updated_at"].isoformat()
        dictrepr["__class__"] = self.__class__.__name__
        return dictrepr

    def __str__(self):
        """Retuns a string representaion of the instance"""

        name = self.__class__.__name__
        string = "[{}] ({}) {}".format(str(name), self.id, self.__dict__)
        return string
