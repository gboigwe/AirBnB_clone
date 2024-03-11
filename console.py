#!/usr/bin/python3
"""
Creating a command prompt
    It runs the console that handles basic:
        create
        read
        update
        delete
        update
"""


import cmd
import uuid
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Impliment a command line action"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        model = args[0]
        if model != "BaseModel":
            print("** class doesn't exist **")
            return
        create_instance = BaseModel()
        create_instance.save()
        print(create_instance)

    

    def emptyline(self):
        """This prevents repeating the previous action
            Rather it turns to a new line waiting for
            next action call"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
