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
        Retrieves all available models
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        models_dict = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
        }
        return models_dict

    def reload(self):
        """
        Deserialises the JSON file into the __objects dictionary
        """
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as storage_file:
            object_str_dict = json.loads(storage_file.read())
        models = self.models()
        for key, value in object_str_dict.items():
            models_key = key.split(".")[0]
            FileStorage.__objects[key] = models[models_key](**value)
