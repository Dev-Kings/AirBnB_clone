#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import json
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Test cases for the console module.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up after the test case.
        """
        pass

    def test_do_create(self):
        """
        Test the do_create method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if UUID is printed

    def test_do_show(self):
        """
        Test the do_show method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show("BaseModel 1234-1234-1234")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        """
        Test the do_destroy method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy("BaseModel 1234-1234-1234")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update(self):
        """
        Test the do_update method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update("BaseModel 1234-1234-1234 name 'test'")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_quit(self):
        """
        Test the do_quit method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_quit(""))
            self.assertEqual(fake_out.getvalue(), "")

    def test_do_EOF(self):
        """
        Test the do_EOF method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_EOF(""))


if __name__ == '__main__':
    unittest.main()
