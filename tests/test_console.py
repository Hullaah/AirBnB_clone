"""This module contains the tests for the console of the application
"""


from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import os


class TestHelp(unittest.TestCase):
    """This is the testcase for the help command of the airbnb console
    """

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            help = ("\nDocumented commands (type help <topic>):\n" +
                    "========================================\n" +
                    "EOF  all  create  destroy  help  quit  show  update\n\n"
                )
            self.assertEqual(help, f.getvalue())
    def test_help_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            help = ("You can use help <command> to get help for a command.\n" +
                    "Usage: help [COMMAND]\n"
                    "Alternative usage: ? [COMMAND]\n"
                )
            self.assertEqual(help, f.getvalue())

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            help = "Press Ctrl + D to exit the console\n"
            self.assertEqual(help, f.getvalue())

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            help = (
                "Shows all model instances or only model instances of a" +
                " particular type\n" + "To show all models:\n" + "Usage: all\n"
                "To show only models of a particular type:\n" +
                "Usage: all [MODEL_TYPE]\n"
            )
            self.assertEqual(help, f.getvalue())

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            help = (
                "Creates a new model and saves.\nUsage: create [MODEL_TYPE]\n"
            )
            self.assertEqual(help, f.getvalue())

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            help = (
                "Deletes a particular model instance.\nUsage: destroy [MODEL_TYPE] [ID]\n"
            )
            self.assertEqual(help, f.getvalue())

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            help = (
                "Quit command to exit the console.\nUsage: quit\n"
            )
            self.assertEqual(help, f.getvalue())

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            help = (
                "Shows a model instance.\nUsage: show [MODEL_TYPE] [ID]\n"
            )
            self.assertEqual(help, f.getvalue())

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            help = (
                "Updates an attribute of a model instance\n" +
                "Usage: update [MODEL_TYPE] [ID] [ATTRIBUTE] [NEW_VALUE]\n"
            )


class TestEOFandQuit(unittest.TestCase):
    """This is the test case for the EOF command (Ctrl + d)
    """

    def test_eof(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue())

class TestCreate(unittest.TestCase):
    """This is the test case for the create command
    """

    def delete_file(self):
        """
        Deletes file.json
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

