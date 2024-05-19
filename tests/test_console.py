#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        # Clean up created files
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_do_quit(self):
        # Test quit command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_quit(""))
        self.assertEqual(fake_out.getvalue().strip(), "")

    def test_do_EOF(self):
        # Test EOF (Ctrl-D) command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_EOF(""))
        self.assertEqual(fake_out.getvalue().strip(), "")

    def test_do_create(self):
        # Test create command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("User")
        self.assertNotEqual(fake_out.getvalue().strip(), "")

    def test_do_show(self):
        # Test show command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show("")
        self.assertIn("** class name missing **", fake_out.getvalue().strip())

    def test_do_destroy(self):
        # Test destroy command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy("")
        self.assertIn("** class name missing **", fake_out.getvalue().strip())

    def test_do_all(self):
        # Test all command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("")
        self.assertIn("** class name missing **", fake_out.getvalue().strip())

    def test_do_update(self):
        # Test update command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update("")
        self.assertIn("** class name missing **", fake_out.getvalue().strip())

    def test_emptyline(self):
        # Test emptyline method
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.emptyline()
        self.assertEqual(fake_out.getvalue().strip(), "")

    # Additional Tests for Default Command Handling

    def test_default_unknown_syntax(self):
        # Test default method for unknown syntax
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("unknown syntax")
        self.assertIn("** Unknown syntax:", fake_out.getvalue().strip())

    def test_default_all(self):
        # Test default method for <class name>.all() command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.all()")
        self.assertIn("** class doesn't exist **", fake_out.getvalue().strip())

    def test_default_count(self):
        # Test default method for <class name>.count() command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.count()")
        self.assertIn("** class doesn't exist **", fake_out.getvalue().strip())

    def test_default_show(self):
        # Test default method for <class name>.show() command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.show()")
        self.assertIn("** instance id missing **", fake_out.getvalue().strip())

    def test_default_destroy(self):
        # Test default method for <class name>.destroy() command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.destroy()")
        self.assertIn("** instance id missing **", fake_out.getvalue().strip())

    def test_default_update(self):
        # Test default method for <class name>.update() command
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.update()")
        self.assertIn("** instance id missing **", fake_out.getvalue().strip())

    def test_default_update_dict(self):
        # Test default method for <class name>.update() command with dictionary
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("User.update()")
        self.assertIn("** instance id missing **", fake_out.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
