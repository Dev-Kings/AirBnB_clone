import unittest

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_save_method(self):
        """
            Test the save method to ensure it updates the updat
            attribute with the current datetime.
        """
        cls = BaseModel()
        updated_time_before = cls.updated_at
        cls.save()
        updated_time_after = cls.updated_at
        self.assertNotEqual(updated_time_before, updated_time_after)
