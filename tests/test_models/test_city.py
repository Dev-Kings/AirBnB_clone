#!/usr/bin/python3
"""Unit tests for the City module."""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

# Create instances of the City class
city1 = City()
city2 = City(**city1.to_dict())
city3 = City("hello", "wait", "in")


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_parameters(self):
        """Test method for class attributes."""
        key = f"{type(city1).__name__}.{city1.id}"
        self.assertIsInstance(city1.name, str)
        self.assertEqual(city3.name, "")
        city1.name = "Abuja"
        self.assertEqual(city1.name, "Abuja")

    def test_initialization(self):
        """Test method for public instances."""
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)
        self.assertEqual(city1.updated_at, city2.updated_at)

    def test_save_method(self):
        """Test method for save."""
        old_update = city1.updated_at
        city1.save()
        self.assertNotEqual(city1.updated_at, old_update)

    def test_to_dict_method(self):
        """Test method for dict."""
        city_dict = city2.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], type(city2).__name__)
        self.assertIn('created_at', city_dict.keys())
        self.assertIn('updated_at', city_dict.keys())
        self.assertNotEqual(city1, city2)


if __name__ == "__main__":
    unittest.main()
