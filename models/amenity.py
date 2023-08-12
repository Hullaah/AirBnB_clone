#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the Amenity
class which inherits from the BaseModel class to represent
an amenity
"""


from .base_model import BaseModel


class Amenity(BaseModel):
    """This is the amenity that represents each amenity of the application

    Attributes:
        name (string): amenity name
    """
    name = ""
