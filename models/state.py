# models/state.py

from models.base_model import BaseModel

class State(BaseModel):
    """ State class inherits from BaseModel """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
