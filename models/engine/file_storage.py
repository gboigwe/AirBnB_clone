#!/usr/bin/python3
"""
Handles the serialization and deserialization
of transfer of json formation
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage: Handles what is stored,
        all dictionary being returned
        reload the stored json
    """

    __file_path = "file.json"
    __objects = {}
    all_class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    def all(self):
        """
        Calls and return all object
        """

        return self.__objects

    def new(self, obj):
        """Creates a new instance of the class
            with a new id
        """

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
            file path: __file_path = "file.json"
            And stores the json file
        """

        got_obj = self.__objects
        my_obj = {}
        for obj_key, obj_val in got_obj.items():
            my_obj[obj_key] = obj_val.to_dict()
        with open(self.__file_path, "w") as fjd:
            json.dump(my_obj, fjd)

    def reload(self):
        """
        Deserializes the json that has been stored to
        a dictionary
        From JSON to DICTIONARY
        """

        try:
            with open(self.__file_path, "r") as fjl:
                my_obj = json.load(fjl)
            for obj_key, obj_data in my_obj.items():
                obj_instance = self.all_class_dict[obj_data['__class__']](**obj_data)
                self.__objects[obj_key] = obj_instance
        except FileNotFoundError:
            pass
