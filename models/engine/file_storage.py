#!/usr/bin/python3
'''
This module helps to save previous objects
in JSON format and load them on tsartup of the console
This saves previous data
'''


import json
import os


class FileStorage:
    """
    This is a file storage class that aids storage of existing
    instance of the BaseModel class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the __objects attribute
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the new obj in __objects
        """
        name = obj.__class__.__name__
        id = obj.id
        FileStorage.__objects[f"{name}.{id}"] = obj

    def save(self):
        """
        This method is used to save the objects to the JSON path __file_path
        """
        object_str_dict = {}
        for key, obj in FileStorage.__objects.items():
            object_str_dict[key] = obj.to_dict()
        object_str_dict = json.dumps(object_str_dict)
        with open(FileStorage.__file_path, "w") as storage_file:
            storage_file.write(object_str_dict)

    def models(self):
        """
        Returns a dict of valid models/classes
        """
        from ..base_model import BaseModel
        from ..amenity import Amenity
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User
        models = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        return models

    def reload(self):
        """
        Deserialises the JSON file into the __objects dictionary
        """
        if not os.path.exists(FileStorage.__file_path):
            return
        __MODELS = self.models()
        with open(FileStorage.__file_path, "r") as storage_file:
            object_str_dict = json.loads(storage_file.read())
        for key, value in object_str_dict.items():
            class_name = value["__class__"]
            FileStorage.__objects[key] = __MODELS[class_name](**value)
