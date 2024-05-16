#!/usr/bin/python3
"""BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Instance attributes."""
        self.updated_at = datetime.now()
        if kwargs:
            self.__dict__['id'] = kwargs['id']
            self.__dict__['name'] = kwargs['name']
            self.__dict__['my_number'] = kwargs['my_number']
            self.__dict__['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            self.__dict__['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.__import__storage().new(self)

    def __str__(self):
        """String rep of class instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates public instance updated_at with the current datetime."""
        self.updated_at = datetime.now()
        self.__import__storage().save()

    def to_dict(self):
        """Converts instance to dictionary.
        Return:
            Dictionary of all key/values of __dict__ of the instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep

    def __import__storage(self):
        """Imports storage only when needed.
        This prevents 'circular import error'."""
        from models import storage
        return storage
