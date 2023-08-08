#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the State
class which inherits from the BaseModel class to represent
a state
"""


from .base_model import BaseModel


class State(BaseModel):
    """This is the state that represents each state of the application

    Attributes:
        name (string): state name
    """
    name = ""
