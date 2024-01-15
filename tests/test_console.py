#!/usr/bin/python3
"""Test cases for console.py"""
import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Redirect stdout for testing"""
        sys.stdout = StringIO()

    def tearDown(self):
        """Reset redirect."""
        sys.stdout = sys.__stdout__

    def test_create_with_params(self):
        """Test create with parameters"""
        console = HBNBCommand()
        with unittest.mock.patch('sys.stdin', StringIO('create Place name="My_house"\n')):
            console.onecmd('')

        self.assertNotEqual(sys.stdout.getvalue().strip(), "** class name missing **")
        self.assertNotEqual(sys.stdout.getvalue().strip(), "** class doesn't exist **")
        self.assertNotEqual(sys.stdout.getvalue().strip(), "** value missing **")
        self.assertNotEqual(sys.stdout.getvalue().strip(), "** attribute name missing **")

if __name__ == "__main__":
    unittest.main()
