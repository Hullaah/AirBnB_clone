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

    def new(self, obj: object):
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

    def reload(self):
        """
        Deserialises the JSON file into the __objects dictionary
        """
        from ..base_model import BaseModel
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as storage_file:
            object_str_dict = json.loads(storage_file.read())
        for key, value in object_str_dict.items():
            FileStorage.__objects[key] = BaseModel(**value)
