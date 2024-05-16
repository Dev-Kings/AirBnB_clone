# models/engine/file_storage.py

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(serialized_objs, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                serialized_objs = json.load(json_file)
                for key, obj_dict in serialized_objs.items():
                    class_name = key.split('.')[0]
                    if class_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**serialized_objs)
