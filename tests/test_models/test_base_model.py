"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It is used to test the BaseModel
class
"""
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestPublicInstanceAttributes(unittest.TestCase):
    """Test case for the public instance attributes of the BaseModel
    class

    Attributes:
        Empty (No attributes)
    """

    def setUp(self) -> None:
        """This is the method to be called before executing each test
        method
        """
        self.model = BaseModel()

    def tearDown(self) -> None:
        """This is the method to be called after executing each test
        method
        """
        del self.model

    def test_id(self):
        """This is the test method that tests the BaseModel public
        instance id attribute.
        """
        self.assertTrue(isinstance(self.model.id, str))

    def test_created_at(self):
        """This is the test method that tests the BaseModel public
        instance created_at attribute.
        """
        self.assertTrue(isinstance(self.model.created_at, datetime.datetime))

    def test_updated_at(self):
        """This is the test method that tests the BaseModel public
        instance updated_at attribute.
        """
        self.assertTrue(isinstance(self.model.updated_at, datetime.datetime))


class TestInstantiateBaseModelFromDict(unittest.TestCase):
    """Test case for the instatntiation of a BaseModel object
    from a dictionary

    Attributes:
        Empty (No attributes)
    """

    def setUp(self) -> None:
        """This is the method to be called before executing each test
        method
        """
        self.dict = {}
        self.dict["id"] = str(uuid.uuid4())
        self.dict["created_at"] = datetime.datetime.now().isoformat()
        self.dict["updated_at"] = self.dict["created_at"]
        self.model_from_dict = BaseModel(**self.dict)

    def tearDown(self) -> None:
        """This is the method to be called after executing each test
        method
        """
        del self.model_from_dict
        del self.dict

    def test_id(self):
        """This is the test method that tests the BaseModel public
        instance id attribute.
        """
        self.assertIsInstance(self.model_from_dict.id, str)
        self.assertEqual(self.model_from_dict.id, self.dict["id"])

    def test_created_at(self):
        """This is the test method that tests the BaseModel public
        instance created_at attribute.
        """
        created_at = datetime.datetime.fromisoformat(self.dict["created_at"])
        self.assertIsInstance(self.model_from_dict.created_at,
                              datetime.datetime)
        self.assertEqual(created_at, self.model_from_dict.created_at)

    def test_updated_at(self):
        """This is the test method that tests the BaseModel public
        instance updated_at attribute.
        """
        updated_at = datetime.datetime.fromisoformat(self.dict["updated_at"])
        self.assertIsInstance(self.model_from_dict.updated_at,
                              datetime.datetime)
        self.assertEqual(updated_at,
                         self.model_from_dict.updated_at)


class TestDunderMethods(unittest.TestCase):
    """Test case for the dunder methods of the BaseModel
    class

    Attributes:
        Empty (No attributes)
    """

    def setUp(self) -> None:
        """This is the method to be called before executing each test
        method"""
        self.model = BaseModel()
        self.model_string = str(self.model)

    def tearDown(self) -> None:
        """This is the method to be called after executing each test
        method"""
        del self.model_string
        del self.model

    def test__str__(self):
        """Thisi s the test method that tests the __str__ magic method
        of the BaseModel class
        """
        test_string = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(self.model_string, test_string)


class TestPublicInstanceMethodSave(unittest.TestCase):
    """Test case for the public instance methods of the BaseModel
    class

    Attributes:
        Empty (No attributes)
    """

    def setUp(self) -> None:
        """This is the method to be called before executing each test
        method"""
        self.model = BaseModel()

    def tearDown(self) -> None:
        """This is the method to be called after executing each test
        method"""
        del self.model

    def test_save(self):
        """This test method tests the save public instance method of the
        BaseModel class
        """
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, prev_updated_at)


class TestPublicInstanceMethodToDict(unittest.TestCase):
    """Test case for the public instance methods of the BaseModel
    class

    Attributes:
        Empty (No attributes)
    """

    def setUp(self) -> None:
        """This is the method to be called before executing each test
        method"""
        self.model = BaseModel()
        self.model_dict = self.model.to_dict()

    def tearDown(self) -> None:
        """This is the method to be called after executing each test
        method"""
        del self.model_dict
        del self.model

    def test_model_dict_contains_keys_and_values_of__dict__(self):
        """This test method tests that the self.model_dict
        contains all the keys and values in self.model__dict__
        """
        for key in self.model.__dict__:
            self.assertIn(key, self.model_dict)
            self.assertEqual(self.model.__dict__[key], self.model_dict[key])

    def test_model_dict_contains_the__class__key(self):
        """tests that the self.model_dict contains the __class__ key and they
        both have the same value
        """
        self.assertIn("__class__", self.model_dict)
        self.assertEqual(self.model_dict["__class__"], "BaseModel")

    def test_created_at_and_updated_at_keys_in_isoformat(self):
        """tests that created at and updated at keys
        have their values in isoformat
        """
        self.assertIsInstance(self.model_dict["created_at"], str)
        self.assertIsInstance(self.model_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
