#!/usr/bin/python3
'''
Module to test the file storage class
Using unittest module
Tests all methods and functionality
'''


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Tests all method of the file storage
    """
    def setUp(self):
        """
        setup method for each test
        """
        self.delete_file()
        self.new_model = BaseModel()
        self.new_model.save()
        storage.reload()

    def tearDown(self) -> None:
        """
        tear down method before each test
        """
        self.delete_file()
        del self.new_model

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

    def test_save_model(self):
        """
        Tests saving of a BaseModel
        """
        self.assertIn(f"BaseModel.{self.new_model.id}", storage.all().keys())

    def test_save_model_2(self):
        """
        Tests saving of a base model
        """
        with open("file.json", "r") as json_file:
            self.assertIn(f"BaseModel.{self.new_model.id}", json_file.read())

    def test_all_method(self):
        """
        tests all method for the FileStorage class
        """
        self.assertIn(f"BaseModel.{self.new_model.id}", storage.all().keys())

    def test_reload_method(self):
        """
        test reload method
        """
        another_model = BaseModel()
        another_model.save()
        storage.reload()
        self.assertIn(f"BaseModel.{another_model.id}", storage.all().keys())
        del another_model

    def test_new_method(self):
        """
        test new method
        """
        another_model = BaseModel()
        self.assertIn(f"BaseModel.{another_model.id}", storage.all().keys())

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
            storage.new(self.new_model, BaseModel())

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
            storage.all(self.new_model)


if __name__ == "__main__":
    unittest.main()
