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

    def test_file_path_exists(self):
        """Test if __file_path is defined."""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects_initialization(self):
        """Test if __objects is initialized as a dictionary and initially empty."""
        self.storage._FileStorage__objects.clear()
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertEqual(len(self.storage._FileStorage__objects), 0)


    def test_all_method(self):
        """Test the all method returns the __objects dictionary."""
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new_method(self):
        """Test new method adds an object to __objects."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        key = f"{type(test_obj).__name__}.{test_obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test if save properly saves objects to file."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file_path))

    def test_reload_method(self):
        """Test reload method correctly loads objects."""
        test_obj = BaseModel()
        test_obj.name = "Test"
        self.storage.new(test_obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f"BaseModel.{test_obj.id}"
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].name, "Test")

    def test_save_correct_content(self):
        """Test if the content of the save file is correct."""
        test_obj = BaseModel()
        self.storage.new(test_obj)
        self.storage.save()
        key = f"{type(test_obj).__name__}.{test_obj.id}"
        with open(self.file_path, 'r') as f:
            content = json.load(f)
        self.assertIn(key, content)

    def test_reload_nonexistent_file(self):
        """Test reloading when file doesn't exist."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.fail("reload() raised an exception on nonexistent file")

    def test_reload_invalid_json(self):
        """Test reloading with invalid JSON."""
        with open(self.file_path, 'w') as f:
            f.write('{"invalid": "json"}')
        with self.assertRaises(Exception):
            self.storage.reload()

    def test_multiple_objects(self):
        """Test saving and reloading multiple objects."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        key1 = f"BaseModel.{obj1.id}"
        key2 = f"BaseModel.{obj2.id}"
        self.assertIn(key1, self.storage.all())
        self.assertIn(key2, self.storage.all())

    def test_overwrite_on_save(self):
        """Test if save overwrites existing file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        obj2 = BaseModel()
        self.storage.new(obj2)
        self.storage.save()

        with open(self.file_path, 'r') as f:
            content = json.load(f)
        self.assertIn(f"BaseModel.{obj2.id}", content)

    def test_data_persistence(self):
        """Test data persistence between FileStorage instances."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", new_storage.all())

    def test_reload_empty_file(self):
        """Test reload with an empty file."""
        with open(self.file_path, 'w') as f:
            pass

        with self.assertRaises(json.decoder.JSONDecodeError):
            self.storage.reload()

    def test_integrity_of_reloaded_objects(self):
        """Test the integrity of objects reloaded from file."""
        obj = BaseModel()
        obj.name = "Test Name"
        self.storage.new(obj)
        self.storage.save()

        self.storage.reload()
        reloaded_obj = self.storage.all()[f"BaseModel.{obj.id}"]
        self.assertEqual(reloaded_obj.name, "Test Name")

    def test_exception_handling_save_reload(self):
        """Test exception handling on save and reload."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.fail("reload() should not raise an exception")


if __name__ == '__main__':
    unittest.main()
