#!/usr/bin/python3
"""Test file for the BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains test cases of BaseModel class."""
    def setUp(self):
        """
        Set up a new instance of BaseModel for testing.
        """
        self.instance = BaseModel()

    def test_attributes(self):
        """
        Test that a BaseModel instance has the correct attributes
        upon initialization """
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_str_method(self):
        """ Test the __str__ method to ensure it returns the correct
        string representation. """
        instance_str_rep = str(self.instance)
        name = self.instance.__class__.__name__
        inst_dict = self.instance.__dict__
        expected_str_rep = f"[{name}] ({self.instance.id}) {inst_dict}"
        self.assertEqual(instance_str_rep, expected_str_rep)

    def test_to_dict_method(self):
        """ Test the to_dict method to ensure it returns a
        dictionary with the correct keys and values, including
        correctly formatted datetime attributes. """
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)

        self.assertIn("__class__", instance_dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")

        self.assertIn("id", instance_dict)
        self.assertEqual(instance_dict["id"], self.instance.id)

        self.assertIn("created_at", instance_dict)
        self.assertEqual(instance_dict["created_at"],
                         self.instance.created_at.isoformat())

        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict["updated_at"],
                         self.instance.updated_at.isoformat())

        for key, value in self.instance.__dict__.items():
            if key not in ["created_at", "updated_at"]:
                self.assertEqual(instance_dict[key], value)

    def test_init_with_kwargs(self):
        """ Test the __init__ method to ensure it correctly
        initializes an instance when provided with a dictionary
        of attributes (kwargs) """
        dummy_data = {
                "id": "123",
                "created_at": "2024-05-15T14:47:43.382659",
                "updated_at": "2024-05-15T14:48:39.231418",
                "name": "Example"
                }

        self.instance = BaseModel(**dummy_data)
        self.assertEqual(self.instance.id, "123")
        self.assertEqual(self.instance.created_at, datetime.fromisoformat(
            "2024-05-15T14:47:43.382659"))
        self.assertEqual(self.instance.updated_at, datetime.fromisoformat(
            "2024-05-15T14:48:39.231418"))
        self.assertEqual(self.instance.name, "Example")

    def test_attributes(self):
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
