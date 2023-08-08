#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the code for
the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


all_class_names = ["BaseModel"]
class HBNBCommand(cmd.Cmd):
    """This is the class for the entry point of the
    command interpreter

    Attributes:
        prompt: prompt for the command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Quits the command inperpreter program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg: str) -> bool | None:

        return super().do_help(arg)

    def emptyline(self):
        """method to be invoked when the user inputs nothing
        on a line and presses ENTER key
        """
        pass

    def do_create(self, arg) -> bool:
        """ create: create [ARG]
        ARG : class name of object to create
        SYNOPSIS : creates a new instance of [ARG], saves it (to file.json)
                    and prints the id
        EXAMPLE : create BaseModel
        """
        classes = [
            {"class_name": "BaseModel","class_creator": create_basemodel}
        ]
        if not arg:
            print("** class name missing **")
            return False
        if arg not in all_class_names:
            print("** class doesn't exist **")
            return False
        for elements in classes:
            if arg == elements["class_name"]:
                elements["class_creator"]()
                return False
        return False

    def do_show(self, arg):
        """show: show [CLASS] [ID]
        ARG : class name of object to show
        SYNOPSIS : prints the string representation od an instance based on
                    the class name and id
        EXAMPLE : show BaseModel ffde2-a345-67e3-2ed3
        """
        args = arg.split()
        if args[0] not in all_class_names:
            print("** class doesn't exist **")
            return False
        print(FileStorage().all()[f"{args[0]}.{args[1]}"])

    def help_help(self):
        """method called when help help is inputed at the command
        interpreter
        """
        print("list available command with 'help' or detailed help ", end="")
        print("with 'help cmd'")

def create_basemodel():
    """Dispatch function called when create is supplied with BaseModel argument
    at the command interpreter
    """
    new_base_model = BaseModel()
    new_base_model.save()
    print(new_base_model.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
