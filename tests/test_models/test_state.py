#!/usr/bin/python3
"""Unit tests for the `state` module."""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """Test method for public instances"""
        state1 = State()
        state2 = State(**state1.to_dict())
        self.assertIsInstance(state1.id, str)
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)
        self.assertEqual(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        """Test method for str representation"""
        state1 = State()
        string = f"[{type(state1).__name__}] ({state1.id}) {state1.__dict__}"
        self.assertEqual(state1.__str__(), string)

    def test_save_method(self):
        """Test method for save"""
        state1 = State()
        old_update = state1.updated_at
        state1.save()
        self.assertNotEqual(state1.updated_at, old_update)

    def test_to_dict_method(self):
        """Test method for dict"""
        state1 = State()
        state2 = State(**state1.to_dict())
        state_dict = state2.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], type(state2).__name__)
        self.assertIn('created_at', state_dict.keys())
        self.assertIn('updated_at', state_dict.keys())
        self.assertNotEqual(state1, state2)


if __name__ == "__main__":
    unittest.main()
