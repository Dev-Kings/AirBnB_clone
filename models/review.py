# models/review.py

class Review(BaseModel):
    """ Review class inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initializes a new Review instance. """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
