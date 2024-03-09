#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
            file path: __file_path = "file.json"
        """
        got_obj = self.__objects
        my_obj = {}
        for obj_key, obj_val in got_obj.items():
            my_obj[obj_key] = obj_val.to_dict()
        with open(self.__file_path, "w") as fjd:
            json.dump(my_obj, fjd)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, "r") as fjl:
                my_obj = json.load(fjl)
                for obj_key, obj_data in my_obj.items():
                    class_name, obj_id = obj_key.split('.')
                    obj_class = eval(class_name)
                    obj_instance = obj_class(**obj_data)
                    self.__objects[obj_key] = obj_instance
        except json.JSONDecodeError:
            print("Invalid JSON data in the file")
