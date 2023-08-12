"""This module contains the tests for the Amenity class
"""


import unittest
import os
from models.amenity import Amenity
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityAttributes(unittest.TestCase):
    """Test case for the Amenity class
    """
    def setUp(self) -> None:
        """setup method called before each test method gets executed
        """
        self.amenity = Amenity()

    def tearDown(self) -> None:
        """tearDown method called after each test method gets executed
        """
        del self.amenity

    def test_name(self):
        """this method tests the amenity name class attribute
        """
        self.assertIsInstance(self.amenity.name, str)


class TestAmenityFileStorage(unittest.TestCase):
    def setUp(self):
        """
        setup method for each test
        """
        self.delete_file()
        self.new_amenity = Amenity()
        self.new_amenity.save()
        storage.reload()

    def tearDown(self) -> None:
        """
        tear down method before each test
        """
        self.delete_file()
        del self.new_amenity

    def delete_file(self):
        """
        Deletes file.json
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_storage_creation(self):
        """
        Tests the storage variable
        """
        self.delete_file()
        self.assertEqual(storage.__class__.__name__, "FileStorage")

    def test_all_method(self):
        """
        Tests the all method for the console
        """
        self.delete_file()
        self.assertEqual(storage.all(), {})

    def check_attributes(self):
        """
        Checks attributes in FileStorage class
        """
        self.delete_file()
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_save_amenity(self):
        """
        Tests saving of a Amenity
        """
        self.assertIn(f"Amenity.{self.new_amenity.id}", storage.all().keys())

    def test_save_amenity_2(self):
        """
        Tests saving of a base amenity
        """
        with open("file.json", "r") as json_file:
            self.assertIn(f"Amenity.{self.new_amenity.id}", json_file.read())

    def test_all_method(self):
        """
        tests all method for the FileStorage class
        """
        self.assertIn(f"Amenity.{self.new_amenity.id}", storage.all().keys())

    def test_reload_method(self):
        """
        test reload method
        """
        another_amenity = Amenity()
        another_amenity.save()
        storage.reload()
        self.assertIn(f"Amenity.{another_amenity.id}", storage.all().keys())
        del another_amenity

    def test_new_method(self):
        """
        test new method
        """
        another_amenity = Amenity()
        self.assertIn(f"Amenity.{another_amenity.id}", storage.all().keys())

    def test_new_no_args(self):
        """
        tests new method with no args
        """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_wrong_args(self):
        """
        tests new method with wrong args
        """
        with self.assertRaises(AttributeError):
            storage.new("Hello")

    def test_new_wrong_args_2(self):
        """
        tests new method with wrong args
        """
        with self.assertRaises(AttributeError):
            storage.new(92)
            storage.new([42, 21])

    def test_new_wrong_args_3(self):
        """
        tests new method with wrong args
        """
        with self.assertRaises(AttributeError):
            storage.new(42.2)

    def test_new_many_args(self):
        """
        tests new method with too many args
        """
        with self.assertRaises(TypeError):
            storage.new(self.new_amenity, Amenity())

    def test_reload_args(self):
        """
        try reload with args
        """
        with self.assertRaises(TypeError):
            storage.reload(92)

    def test_save_args(self):
        """
        tests save method with args
        """
        with self.assertRaises(TypeError):
            storage.save("red")

    def test_all_args(self):
        """
        tests all method with args
        """
        with self.assertRaises(TypeError):
            storage.all(self.new_amenity)


if __name__ == "__main__":
    unittest.main()
