#!/usr/bin/python3
""" Unit test for FileStorage class """

import unittest
from unittest.mock import patch, mock_open
from models.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os


class TestFileStorage(unittest.TestCase):
    """ Define Test Cases for FileStorage Class """

    def setUp(self):
        """ Set up test methods """
        FileStorage._FileStorage__objects = {}
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.key = f"{self.obj.__class__.__name__}.{self.obj.id}"

    def test_all(self):
        """ Test all method """
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        """ Test new method """
        self.storage.new(self.obj)
        self.assertIn(self.key, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[self.key], self.obj)

    @patch('models.file_storage.open', new_callable=mock_open)
    def test_save(self, mock_file):
        """ Test save method """
        self.storage.new(self.obj)
        self.storage.save()
        mock_file.assert_called_once_with(FileStorage._FileStorage__file_path, 'w')
        handle = mock_file()
        handle.write.assert_called_once_with(json.dumps({self.key: self.obj.to_dict()}))

    @patch('models.file_storage.open', new_callable=mock_open,
    read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}')
    def test_reload(self, mock_file):
        """ Test reload method """
        self.storage.reload()
        mock_file.assert_called_once_with(FileStorage._FileStorage__file_path, 'r')
        self.assertIn('BaseModel.1234', FileStorage._FileStorage__objects)
        self.assertIsInstance(FileStorage._FileStorage__objects['BaseModel.1234'], BaseModel)

    def tearDown(self):
        """ Clean up tasks """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
