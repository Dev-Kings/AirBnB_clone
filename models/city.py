# models/city.py

class City(BaseModel):
    """City class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Initializes a new City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
