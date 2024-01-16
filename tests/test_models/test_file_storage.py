#!/isr/bin/python3
"""Unit test for the FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test methods."""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up tasks."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test if all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test if new properly adds objects."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        key = f"{type(test_obj).__name__}.{test_obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if save properly saves objects to file."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test if reload properly loads objects from file."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        self.storage.save()
        self.storage.reload()
        key = f"{type(test_obj).__name__}.{test_obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
