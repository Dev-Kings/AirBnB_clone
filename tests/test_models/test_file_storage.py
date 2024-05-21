import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """
        Clean up test environment.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        FileStorage._FileStorage__objects = {}

    def test_file_path_exists(self):
        """
        Test that __file_path is defined.
        """
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_exists(self):
        """
        Test that __objects is defined.
        """
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_returns_dict(self):
        """
        Test that all returns the __objects dictionary.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """
        Test that new adds an object to __objects.
        """
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """
        Test that save creates a file.
        """
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_save_content(self):
        """
        Test that save correctly serializes objects to file.
        """
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            content = f.read()
            self.assertIn(self.model.id, content)

    def test_reload(self):
        """
        Test that reload correctly deserializes objects from file.
        """
        self.storage.save()  # Ensure the file is saved before reloading
        self.storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
