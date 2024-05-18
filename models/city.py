#!/usr/bin/python3
# models/city.py

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel

    Attributes:
        state_id (str): The ID of the state to which
            the city belongs.
        name (str): The name of the city

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
                    'state_id' and 'name' are retrieved
                    from kwargs if provided.
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
