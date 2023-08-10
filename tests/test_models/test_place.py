"""This module contains the tests for the Place class
"""


import unittest
import os
from models.place import Place
from models import storage
from models.engine.file_storage import FileStorage


class TestPlaceAttributes(unittest.TestCase):
    """Test case for the Place class
    """
    def setUp(self) -> None:
        """setup method called before each test method gets executed
        """
        self.place = Place()

    def tearDown(self) -> None:
        """tearDown method called after each test method gets executed
        """
        del self.place

    def test_city_id(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.user_id, str)

    def test_name(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.name, str)

    def test_description(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_longitude(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.longitude, float)

    def test_latitude(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.latitude, float)

    def test_amenity_ids(self):
        """this method tests the place name class attribute
        """
        self.assertIsInstance(self.place.amenity_ids, list)
        [self.assertTrue(isinstance(x, str)) for x in self.place.amenity_ids]


class TestPlaceFileStorage(unittest.TestCase):
    def setUp(self):
        """
        setup method for each test
        """
        self.delete_file()
        self.new_place = Place()
        self.new_place.save()
        storage.reload()

    def tearDown(self) -> None:
        """
        tear down method before each test
        """
        self.delete_file()
        del self.new_place

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

    def test_save_place(self):
        """
        Tests saving of a Place
        """
        self.assertIn(f"Place.{self.new_place.id}", storage.all().keys())

    def test_save_place_2(self):
        """
        Tests saving of a base place
        """
        with open("file.json", "r") as json_file:
            self.assertIn(f"Place.{self.new_place.id}", json_file.read())

    def test_all_method(self):
        """
        tests all method for the FileStorage class
        """
        self.assertIn(f"Place.{self.new_place.id}", storage.all().keys())

    def test_reload_method(self):
        """
        test reload method
        """
        another_place = Place()
        another_place.save()
        storage.reload()
        self.assertIn(f"Place.{another_place.id}", storage.all().keys())
        del another_place

    def test_new_method(self):
        """
        test new method
        """
        another_place = Place()
        self.assertIn(f"Place.{another_place.id}", storage.all().keys())

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
            storage.new(self.new_place, Place())

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
            storage.all(self.new_place)


if __name__ == "__main__":
    unittest.main()
