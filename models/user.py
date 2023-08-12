#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the User
class which inherits from the BaseModel class to represent
a user
"""


from .base_model import BaseModel


class User(BaseModel):
    """This is the user that represents each user of the application

    Attributes:
        email (string): user email address
        password (string): user password
        first_name (string): user first name
        last_name (string): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
