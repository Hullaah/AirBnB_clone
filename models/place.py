"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the Place
class which inherits from the BaseModel class to represent
a place
"""

from .base_model import BaseModel


class Place(BaseModel):
    """Ths is the place class that represents each place of the application

    Attributes:
        city_id (string): city id of place
        user_id (string): user id of place
        name (string): name of place
        description (string): description of place
        number_rooms (integer) : number of roomas available in place
        number_bathrooms (integer): number of bathrooms available in place
        max_guest (integer): max guests place can contain
        price_by_night (integer): price of night stay at place
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (list): ids list of amenities in place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
