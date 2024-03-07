#!/usr/bin/python3
"""
    Basemode - This is the base model class
    Other classes will inherit from it
"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """
    Basemodel is created with function modules and methods
        __init__: gets to initialise the class upon call
        __str__: returns the string of the taken variable
        save: stores the updated status
        to_dict: converts all key values to a string
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises the class by assigning appropriate value
            id to a generated random id
            created_at to actual time
            updated_at to updated time
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    c = "%Y-%m-%dT%H:%M:%S.%f"
                    try:
                        setattr(self, key, datetime.strptime(value, c))
                    except ValueError:
                        print("Error: Invalid date format for {}: {}".format(key, value))
                else:
                    setattr(self, key, value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the formated string of class and variables
        """
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        This method updates the variable updated_at
        Assigns a new datetime whenever updated is called
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of all variable action
        """
        s_dict = self.__dict__
        s_dict['__class__'] = self.__class__.__name__
        s_dict['created_at'] = s_dict['created_at'].isoformat()
        s_dict['updated_at'] = s_dict['updated_at'].isoformat()
        return s_dict

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
