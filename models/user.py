#!/usr/bin/python3

"""
user.py

This module defines the User class, a subclass of
BaseModel, which represents users within the application.

Classes:
    User: A class that inherits from BaseModel and
    represents a user with attributes like email, password,
    first_name, and last_name.

Usage:
    This module is typically used as part of a larger
    application that manages different models like users,
    places, states, cities, amenities, and reviews.

Example:
    from models.user import User
    new_user = User(email="john.doe@example.com",
    password="s3cr3t", first_name="John", last_name="Doe")
    new_user.save()

Attributes:
    (No module-level attributes)
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
