#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model1 import BaseModel


class FileStorage:
    """The class serializes instances to a JSON file and deserializes
    JSON file to instances.
    Attributes:
        __file_path: path of file
        __objects: dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Store all objects by id in dictionary.
        Returns:
            Dictionary of __objects.
        """
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        self.__class__.__objects['{obj.__class__.__name__}.id'] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            serialize_objects = {key: obj.to_dict() for key, obj in self.__class__.__objects.items()}
            json.dump(serialize_objects, json_file)

    def reload(self):
        """Deserializes JSON file to __objects.
        If file doesn't exists, just pass."""
        try:
            with open("file.json", "r") as json_file:
                objects_dict = json.load(json_file)
                for key, object_dict in objects_dict.items():
                    cls = globals()[object_dict['__class__']]
                    self.__objects[key] = cls(**object_dict)
        except IOError:
            pass

