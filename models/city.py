#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the City
class which inherits from the BaseModel class to represent
a city
"""


from .base_model import BaseModel


class City(BaseModel):
    """This is the city that represents each city of the application

    Attributes:
        name (string): city name
        state_id (string): state id of city location
    """
    name = ""
    state_id = ""
