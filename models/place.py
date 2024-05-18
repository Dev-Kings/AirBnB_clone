#!/usr/bin/python3
# models/place.py

"""
place.py

This module defines the Place class, a subclass of
BaseModel, which represents places that can be rented
or listed in the application.

Classes:
    Place: A class that inherits from BaseModel and
    represents a place with various attributes like name,
    description, number of rooms, etc.

Usage:
    This module is typically used as part of a larger
    application that manages different models like users,
    places, states, cities, amenities, and reviews.

Example:
    from models.place import Place
    new_place = Place(name="Cozy Cottage", city_id="1234",
    user_id="5678", description="A cozy place to stay",
    number_rooms=3, number_bathrooms=2, max_guest=4,
    price_by_night=100)
    new_place.save()

Attributes:
    (No module-level attributes)
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initializes a new Place instance. """
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', "")
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])
