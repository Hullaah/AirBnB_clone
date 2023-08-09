"""This module contains the tests for the Review class
"""


import unittest
import os
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class TestReviewAttributes(unittest.TestCase):
    """Test case for the Review class
    """
    def setUp(self) -> None:
        """setup method called before each test method gets executed
        """
        self.review = Review()

    def tearDown(self) -> None:
        """tearDown method called after each test method gets executed
        """
        del self.review

    def test_place_id(self):
        """this method tests the review name class attribute
        """
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id(self):
        """this method tests the review name class attribute
        """
        self.assertIsInstance(self.review.user_id, str)

    def test_text(self):
        """this method tests the review name class attribute
        """
        self.assertIsInstance(self.review.text, str)


class TestReviewFileStorage(unittest.TestCase):
    def setUp(self):
        """
        setup method for each test
        """
        self.delete_file()
        self.new_review = Review()
        self.new_review.save()
        storage.reload()

    def tearDown(self) -> None:
        """
        tear down method before each test
        """
        self.delete_file()
        del self.new_review

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

    def test_save_review(self):
        """
        Tests saving of a Review
        """
        self.assertIn(f"Review.{self.new_review.id}", storage.all().keys())

    def test_save_review_2(self):
        """
        Tests saving of a base review
        """
        with open("file.json", "r") as json_file:
            self.assertIn(f"Review.{self.new_review.id}", json_file.read())

    def test_all_method(self):
        """
        tests all method for the FileStorage class
        """
        self.assertIn(f"Review.{self.new_review.id}", storage.all().keys())

    def test_reload_method(self):
        """
        test reload method
        """
        another_review = Review()
        another_review.save()
        storage.reload()
        self.assertIn(f"Review.{another_review.id}", storage.all().keys())
        del another_review

    def test_new_method(self):
        """
        test new method
        """
        another_review = Review()
        self.assertIn(f"Review.{another_review.id}", storage.all().keys())

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
            storage.new(self.new_review, Review())

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
            storage.all(self.new_review)
