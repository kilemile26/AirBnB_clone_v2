#!/usr/bin/python3
"""Test cases for console.py"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(console.py), "../..")))
from console import HBNBCommand
from io import StringIO
import sys
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def test_create_with_params(self):
        """Test 'create' command with parameters"""
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd('create Place name="My_house"')
            output = f.getvalue().strip()
        # Ensure an ID was returned (UUID format expected)
        self.assertRegex(output, r"^[\w-]{36}$")  # Simplified UUID check 
            
    def test_help_show(self):
        """Test 'help show' command outputs usage"""
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd('help show')
            output = f.getvalue()
            self.assertIn("Display the string representation of an instance", output)
 
if __name__ == "__main__":
    unittest.main()