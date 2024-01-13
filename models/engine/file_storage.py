#!/usr/bin/python 3
"""contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}
        obj = FileStorage.__objects[key]

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
       with open(FileStorage.__file_path, 'w') as f:
        json.dumbs(obj_dict, f)

             
    
