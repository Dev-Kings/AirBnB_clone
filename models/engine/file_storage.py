# models/engine/file_storage.py

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ initializes the Filestorage instance. """
        pass

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    # Recreate instances based on class name
                    if class_name == "BaseModel":
                        new_instance = BaseModel(**obj_dict)
                    elif class_name == "User":
                        new_instance = User(**obj_dict)
                    self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
