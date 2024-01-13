#!/usr/bin/python3
"""
File Storage class.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State
}


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances:"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        name = obj.__class__.__name__
        id = obj.id
        self.__objects[name + '.' + id] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        json_obj = {}
        for key, value in self.__objects.items():
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, 'r') as file:
                json_obj = json.load(file)
                for key, value in json_obj.items():
                    self.__objects[key] = classes[value["__class__"]](**value)
        except FileNotFoundError:
            pass
