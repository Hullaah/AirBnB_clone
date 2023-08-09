#!/usr/bin/python3
'''
Console file for the airbnb console project for ALX SE curriculum
This is the main entry point for the console
Defines different methods to enable the user perform commands
'''


import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The main AirBnB console class
    """
    prompt = "(hbnb) "
    __MODELS = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }
    __attributes = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    # Commands - these define the console functionality
    def do_EOF(self, line):
        """
        Defines EOF action
        """
        print()
        return True

    def do_quit(self, line):
        """
        Defines the quit command
        """
        return True

    def do_create(self, line):
        """
        Defines the create command for the console
        """
        args = self.parse_args(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__MODELS.keys():
            print("** class doesn't exist **")
        else:
            new_model = self.__MODELS[args[0]]()
            new_model.save()

    def do_show(self, line):
        """
        Defines the show command for the console
        """
        args = self.parse_args(line)
        model_tuple = self.validity_check(args)
        if model_tuple[0] is False:
            print(model_tuple[1])
            return False
        print(storage.all()[model_tuple[1]])

    def do_destroy(self, line):
        """
        Defines the destroy command for the console
        """
        args = self.parse_args(line)
        model_tuple = self.validity_check(args)
        if model_tuple[0] is False:
            print(model_tuple[1])
            return False
        del storage.all()[model_tuple[1]]
        storage.save()

    def do_all(self, line):
        """
        Implements the all command
        """
        args = self.parse_args(line)
        storage.reload()
        if len(args) == 0:
            print([str(model) for model in storage.all().values()])
        elif args[0] not in self.__MODELS.keys():
            print("** class doesn't exist")
        else:
            print([str(model) for key, model in
                   storage.all().items() if args[0] in key])

    def do_update(self, line):
        """
        Implements the update command for the console
        """
        args = self.parse_args(line)
        model_tuple = self.validity_check(args)
        if model_tuple[0] is False:
            print(model_tuple[1])
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False
        args = args[:4]
        new_value = args[3].strip('"')
        if args[2] in self.__attributes.keys():
            new_value = self.__attributes[args[2]](args[3])
        updated_obj = storage.all()[f"{model_tuple[1]}"]
        setattr(updated_obj, args[2], new_value)
        updated_obj.save()

    # Help - control the help prompts
    def help_help(self):
        """
        Defines help for the help command
        """
        print("You can use help <command> to get help for a command.")
        print("Usage: help [COMMAND]")
        print("Alternative usage: ? [COMMAND]")

    def help_EOF(self):
        """
        Defines help for EOF
        """
        print("Press Ctrl + D to exit the console")

    def help_quit(self):
        """
        Defines help for the quit command
        """
        print("Quit command to exit the console.\nUsage: quit")

    def help_create(self):
        """
        Help for the create command
        """
        print("Creates a new model and saves.\nUsage: create [MODEL_TYPE]")

    def help_show(self):
        """
        Help for the show command
        """
        print("Shows a model instance.\nUsage: show [MODEL_TYPE] [ID]")

    def help_destroy(self):
        """
        Help for the destroy command
        """
        print("Deletes a particular model instance.\nUsage: destroy " +
              "[MODEL_TYPE] [ID]")

    def help_all(self):
        """
        Defines help for the all command
        """
        print("Shows all model instances or only model instances of a " +
              "particular type")
        print("To show all models:")
        print("Usage: all")
        print("To show only models of a particular type: ")
        print("Usage: all [MODEL_TYPE]")

    def help_update(self):
        """
        Defines help for the update command
        """
        print("Updates an attribute of a model instance")
        print("Usage: update [MODEL_TYPE] [ID] [ATTRIBUTE] [NEW_VALUE]")

    # Base functionality for the console
    def emptyline(self):
        """
        Overrides default behaviour for an empty line to not do anything
        """
        pass

    def parse_args(self, args):
        """
        parses the arguments into a tuple
        """
        return tuple(args.split())

    def validity_check(self, args):
        """
        checks if a model exists
        """
        if len(args) == 0:
            return False, "** class name missing **"
        elif args[0] not in self.__MODELS.keys():
            return False, "** class doesn't exist **"
        elif len(args) < 2:
            return False, "** instance id missing **"
        model_key = f"{args[0]}.{args[1]}"
        storage.reload()
        if model_key not in storage.all().keys():
            return False, "** no instance found **"
        return True, model_key


if __name__ == "__main__":
    HBNBCommand().cmdloop()
