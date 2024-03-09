#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Impliment a command line action"""
    prompt = "(hbnb) "
    models = {
            "BaseModel": BaseModel
            }

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        model = args[0]
        if model not in self.models:
            print("** class doesn't exist **")
            return
        create_instance = self.models[model]()
        print(create_instance.id)

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
