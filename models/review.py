#!/usr/bin/python3
"""models/review module
Contains Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel

    Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
            'place_id', 'user_id', and 'text' are
            retrieved from kwargs if provided.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword argumeents.
                'place_id', 'user_id', and 'text' are
                retrieved from kwargs if provided.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
