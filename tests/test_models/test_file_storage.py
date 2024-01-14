#!/isr/bin/python3
"""Unit test for the FileStorage class"""

import unittest
import json
import os
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up for the tests."""
        self.storage = FileStorage()
        self.model = BaseModel()
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method of FileStorage."""
        self.storage.new(self.model)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)

    def test_new(self):
        """Test the new method of FileStorage."""
        self.storage.new(self.model)
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_save(self):
        """Test the save method of FileStorage."""
        FileStorage._FileStorage__objects = {}
        model = BaseModel()
        self.storage.new(model)

        with patch('models.engine.file_storage.open', mock_open(), create=True) as mock_file:
            self.storage.save()
        
            actual_write_calls = ''.join(args[0] for args, _ in mock_file().write.call_args_list)
            expected_output = json.dumps({f"BaseModel.{model.id}": model.to_dict()})  # Default formatting

            self.assertEqual(actual_write_calls, expected_output)

    def test_reload_no_file(self):
        """Test reload method when file does not exist."""
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)


    def test_reload_with_file(self):
        """Test reload method when file exists."""
        self.model.save()
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_save_empty_storage(self):
        """Test save method with no objects."""
        FileStorage._FileStorage__objects = {}  # Clear any pre-existing data
        with patch('models.engine.file_storage.open', mock_open()) as mock_file:
            self.storage.save()

            mock_file.assert_called_with('file.json', 'w')
            written_data = mock_file().write.call_args[0][0]
            self.assertEqual(written_data, '{}')

    def test_reload_invalid_file(self):
        """Test reload with an invalid JSON file."""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write('Invalid JSON')
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_file_storage_integration(self):
        """Integration test for file storage."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)
