"""This module contains the tests for the City class
"""


import unittest
import os
from models.city import City
from models import storage
from models.engine.file_storage import FileStorage


class TestCityAttributes(unittest.TestCase):
    """Test case for the City class
    """
    def setUp(self) -> None:
        """setup method called before each test method gets executed
        """
        self.city = City()

    def tearDown(self) -> None:
        """tearDown method called after each test method gets executed
        """
        del self.city

    def test_name(self):
        """this method tests the city name class attribute
        """
        self.assertIsInstance(self.city.name, str)

    def test_state_id(self):
        """this method tests the city state_id class attribute
        """
        self.assertIsInstance(self.city.state_id, str)


class TestCityFileStorage(unittest.TestCase):
    def setUp(self):
        """
        setup method for each test
        """
        self.delete_file()
        self.new_city = City()
        self.new_city.save()
        storage.reload()

    def tearDown(self) -> None:
        """
        tear down method before each test
        """
        self.delete_file()
        del self.new_city

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

    def test_save_city(self):
        """
        Tests saving of a City
        """
        self.assertIn(f"City.{self.new_city.id}", storage.all().keys())

    def test_save_city_2(self):
        """
        Tests saving of a base city
        """
        with open("file.json", "r") as json_file:
            self.assertIn(f"City.{self.new_city.id}", json_file.read())

    def test_all_method(self):
        """
        tests all method for the FileStorage class
        """
        self.assertIn(f"City.{self.new_city.id}", storage.all().keys())

    def test_reload_method(self):
        """
        test reload method
        """
        another_city = City()
        another_city.save()
        storage.reload()
        self.assertIn(f"City.{another_city.id}", storage.all().keys())
        del another_city

    def test_new_method(self):
        """
        test new method
        """
        another_city = City()
        self.assertIn(f"City.{another_city.id}", storage.all().keys())

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
            storage.new(self.new_city, City())

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
            storage.all(self.new_city)
