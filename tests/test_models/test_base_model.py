#!/usr/bin/python3
"""Unit test for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import uuid


class TestBaseModel(unittest.TestCase):
    """Defines the test cases for the BaseModel class"""

    def test_instance_creation(self):
        """ Test for proper instance creation """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_assignment(self):
        """ Test for id attribute assignment """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertIsInstance(model.id, str)

    def test_created_at_assignment(self):
        """ Test for created_at attribute assignment """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_assignment(self):
        """ Test for updated_at attribute assignment """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.updated_at, datetime)

    def test_time_assignment(self):
        """ Test for proper time assignment """
        model = BaseModel()
        self.assertLessEqual(model.created_at, model.updated_at)

    def test_str_representation(self):
        """ Test the __str__ method """
        model = BaseModel()
        string = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), string)

    def test_save_method(self):
        """ Test the save method """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs_init(self):
        """ Test initialization with kwargs """
        time = datetime.now()
        model = BaseModel(id="1234", created_at=time.isoformat(),
                          updated_at=time.isoformat())
        self.assertEqual(model.id, "1234")
        self.assertEqual(model.created_at, time)
        self.assertEqual(model.updated_at, time)

    def test_kwargs_ignores_class(self):
        """ Test __class__ key in kwargs is ignored """
        model = BaseModel(__class__="ShouldNotChange")
        self.assertNotEqual(model.__class__.__name__, "ShouldNotChange")

    def test_id_uniqueness(self):
        """ Test that each id is unique """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()
