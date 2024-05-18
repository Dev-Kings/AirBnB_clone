#!/usr/bin/python3
"""tests/test_file_storage module
Contains tests om FileStorage class.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Contains test cases on FileStorage"""
    def setUp(self):
        """Set up test case environment."""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.objects = self.storage._FileStorage__objects
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.model = BaseModel()

    def tearDown(self):
        """Clean up test case environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """Test the all method returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), self.objects)

    def test_new_method(self):
        """Test the new method sets the object in __objects
        with the correct key."""
        key = f"BaseModel.{self.model.id}"
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """Test the save method serializes __objects to the JSON file."""
        self.storage.new(self.model)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            json_content = json.load(f)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, json_content)
        self.assertEqual(json_content[key], self.model.to_dict())

    def test_reload_method(self):
        """Test the reload method deserializes the JSON file to __objects."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())
        reloaded_model = self.storage.all()[key]
        self.assertEqual(reloaded_model.id, self.model.id)
        self.assertEqual(reloaded_model.created_at, self.model.created_at)
        self.assertEqual(reloaded_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
