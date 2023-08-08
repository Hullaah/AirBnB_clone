"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the Review
class which inherits from the BaseModel class to represent
a review
"""


from .base_model import BaseModel


class Review(BaseModel):
    """This is the review class that represents each review of the application

    Attributes:
        place_id (string): id of place reviewed
        user_id (string): id of user that reviewed
        text (string): review text
    """
    place_id = ""
    user_id = ""
    text = ""
