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
import re
from shlex import split
import uuid
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Impliment a command line action"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Handling a default behavior for when cmd module
        input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """
        Defining the create command

        Args:
            arg : the argument passed to the command
                    prompt

        Returns:
            Nothing
        """

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
        print(create_instance.id)

    def do_show(self, arg):
        """
        Defining the show command.
        Handles the display of the instances by the
        class id

        Args:
            arg : the argument passed to the command
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        model = args[0]
        if model not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model1 = args[1]
        key_class = "{}.{}".format(model, model1)
        if key_class not in storage.all():
            print("** no instance found **")
            return
        sto_all = storage.all()
        for key, val in sto_all.items():
            print("[{}] ({}) {}".format(
                val.__class__.__name__,
                val.id, val.__dict__))

    def do_destroy(self, arg):
        """Destroy an instance of a model
                                                            
        Args:
            arg: The string with the model name and id
            separated
        Returns: None
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{model_name}.{instance_id}"
        all_instances = storage.all()
        if key not in storage.all():
            print("** no instance found **")
            return
        del all_instances[key]
        storage.save()

    def do_all(self, arg):
        """
        Defining the all command that displays
        all instances when called

        Args:
            args : takes in the argument passed to
                    the command prompt
        """

        args = parse(arg)
        model = args[0]
        if len(arg) > 0 and model not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        sto_all = storage.all()
        lis_key = []
        for key, val in sto_all.items():
            obj = "[{}] ({}) {}".format(
                val.__class__.__name__, val.id,
                val.__dict__)
            lis_key.append(obj.__str__())
        print(lis_key)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Defining the updated command that handles
        the incoming created instances

        Args:
            arg : Checks for the argument passed
        """

        args = parse(arg)

        if not args:
            print("** class name missing **")
            return

        model_name = args[0]
        if model_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key_class = "{}.{}".format(model_name, instance_id)
        if key_class not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        value = args[3]
        some_data = storage.all()[key_class]
        setattr(some_data, attr_name, value)
        storage.save()

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
