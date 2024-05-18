#!/usr/bin/python3
# models/amenity.py

"""
amenity.py

This module defines the Amenity class, a subclass of
BaseModel, which represents amenities that can be
associated with various accommodations or locations.

Classes:
    Amenity: A class that inherits from BaseModel and
    represents an amenity with a name attribute.

Usage:
    This module is typically used as part of a larger
    application that manages different models like users,
    places, states, cities, amenities, and reviews.

Example:
    from models.amenity import Amenity
    new_amenity = Amenity(name="WiFi")
    new_amenity.save()

Attributes:
    (No module-level attributes)
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel

    Attributes:
        name (str): The name of the Amenity.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
            'name' is retrieved from kwargs if provided.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
