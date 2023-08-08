#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the BaseModel
class which is the base class for all our models to be used in
this project.
"""


import uuid
import datetime
from . import storage


class BaseModel:
    """The BaseModel class is the base class for all our
    models to be used in this project.

    Attributes:
        Empty (No attributes)
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialiser of the base class

        Args:
            *args: Tuple that contains all arguments used for object
            instantiation
            **kwargs: Dictionary that contains all arguments by key/value used
            for object instantiation

        Attributes:
            id: unique oinstance identifier
            created_at: date of creation
            updated_at: date updated

        Return:
            None
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.fromisoformat(
                kwargs["created_at"]
                )
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs["updated_at"]
                )

    def save(self) -> None:
        """updates the public instace attribute, updated_at, with the current
        datetime

        Args:
            Empty (No args)

        Return:
            None
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of __dict__ of the
        instance

        Args:
            Empty (No args)

        Return:
            dictionary representation of instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
