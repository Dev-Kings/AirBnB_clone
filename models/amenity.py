#!/usr/bin/python3
# models/amenity.py

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
