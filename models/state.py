#!/usr/bin/python3
# models/state.py

"""
state.py

This module defines the State class, a subclass of
BaseModel, which represents states that can contain
multiple cities within the application.

Classes:
    State: A class that inherits from BaseModel and
    represents a state with a name attribute.

Usage:
    This module is typically used as part of a larger
    application that manages different models like users,
    places, states, cities, amenities, and reviews.

Example:
    from models.state import State
    new_state = State(name="California")
    new_state.save()

Attributes:
    (No module-level attributes)
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
