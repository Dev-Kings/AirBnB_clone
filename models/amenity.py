# models/amenity.py

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Initializes a new Amenity instance. """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
