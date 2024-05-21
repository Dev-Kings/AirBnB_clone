#!/usr/bin/python3
"""
Unit tests for the FileStorage class in models/engine/file_storage.py.

Test classes:
- TestFileStorageInitialization
- TestFileStorageMethods
"""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorageInitialization(unittest.TestCase):
    """
    Test cases for the instantiation of the FileStorage class.
    """

    def test_initialization_no_arguments(self):
        """
        Test creating a FileStorage instance without arguments.
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_initialization_with_arguments(self):
        """
        Test creating a FileStorage instance with arguments.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_file_path_is_string(self):
        """
        Test that __file_path is a private string attribute.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_objects_is_dict(self):
        """
        Test that __objects is a private dictionary attribute.
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initialization(self):
        """
        Test that storage is an instance of FileStorage.
        """
        self.assertEqual(type(storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """
    Test cases for the methods of the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        """
        Test the all() method returns a dictionary.
        """
        self.assertEqual(dict, type(storage.all()))

    def test_all_with_arguments(self):
        """
        Test all() method with arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_method(self):
        """
        Test the new() method adds objects to __objects.
        """
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        self.assertIn(f"BaseModel.{bm.id}", storage.all().keys())
        self.assertIn(bm, storage.all().values())
        self.assertIn(f"User.{us.id}", storage.all().keys())
        self.assertIn(us, storage.all().values())
        self.assertIn(f"State.{st.id}", storage.all().keys())
        self.assertIn(st, storage.all().values())
        self.assertIn(f"Place.{pl.id}", storage.all().keys())
        self.assertIn(pl, storage.all().values())
        self.assertIn(f"City.{cy.id}", storage.all().keys())
        self.assertIn(cy, storage.all().values())
        self.assertIn(f"Amenity.{am.id}", storage.all().keys())
        self.assertIn(am, storage.all().values())
        self.assertIn(f"Review.{rv.id}", storage.all().keys())
        self.assertIn(rv, storage.all().values())

    def test_new_with_extra_arguments(self):
        """
        Test new() method with extra arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_with_none(self):
        """
        Test new() method with None raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_method(self):
        """
        Test the save() method saves objects to file.json.
        """
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        with open("file.json", "r") as f:
            save_content = f.read()
            self.assertIn(f"BaseModel.{bm.id}", save_content)
            self.assertIn(f"User.{us.id}", save_content)
            self.assertIn(f"State.{st.id}", save_content)
            self.assertIn(f"Place.{pl.id}", save_content)
            self.assertIn(f"City.{cy.id}", save_content)
            self.assertIn(f"Amenity.{am.id}", save_content)
            self.assertIn(f"Review.{rv.id}", save_content)

    def test_save_with_arguments(self):
        """
        Test save() method with arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        """
        Test the reload() method loads objects from file.json.
        """
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{bm.id}", objects)
        self.assertIn(f"User.{us.id}", objects)
        self.assertIn(f"State.{st.id}", objects)
        self.assertIn(f"Place.{pl.id}", objects)
        self.assertIn(f"City.{cy.id}", objects)
        self.assertIn(f"Amenity.{am.id}", objects)
        self.assertIn(f"Review.{rv.id}", objects)

    def test_reload_with_arguments(self):
        """
        Test reload() method with arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
