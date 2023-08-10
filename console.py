#!/usr/bin/python3
"""This module is part of the airbnb clone package project done
during the alx SE engineering course. It contains the code for
the entry point of the command interpreter.
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


all_class_names = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review",
]


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
        """ create: create [CLASS]
        CLASS : class name of object to create

        SYNOPSIS : creates a new instance of [ARG], saves it (to file.json)
                    and prints the id

        EXAMPLE : create BaseModel
        """
        classes = [
            {"class_name": "BaseModel", "class_creator": create_basemodel},
            {"class_name": "User", "class_creator": create_user},
            {"class_name": "State", "class_creator": create_state},
            {"class_name": "City", "class_creator": create_city},
            {"class_name": "Amenity", "class_creator": create_amenity},
            {"class_name": "Place", "class_creator": create_place},
            {"class_name": "Review", "class_creator": create_review},
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
        CLASS : class name of object to show
        ID : instance id of object to show

        SYNOPSIS : prints the string representation od an instance based on
                    the class name and id

        EXAMPLE : show BaseModel ffde2-a345-67e3-2ed3
        """
        args = parse_arg(arg)
        try:
            if args[0] not in all_class_names:
                print("** class doesn't exist **")
                return False
        except IndexError:
            print("** class name missing **")
            return False
        else:
            try:
                print(storage.all()[f"{args[0]}.{args[1]}"])
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroy: destroy [CLASS] [ID]
        CLASS : class name of object to destroy
        ID : instance id of object to destroy

        SYNOPSIS :  deletes an instance based on the class name and id

        EXAMPLE : destroy BaseModel ffde2-a345-67e3-2ed3
        """
        args = parse_arg(arg)
        try:
            if args[0] not in all_class_names:
                print("** class doesn't exist **")
                return False
        except IndexError:
            print("** class name missing **")
            return False
        else:
            try:
                del storage.all()[f"{args[0]}.{args[1]}"]
                storage.save()
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """all : all | all [CLASS]
        CLASS (optional) : classname of all instances to be displayed

        SYNOPSIS : displays string representation of all instances based or not
                    on the class name

        EXAMPLE : all
                 all User
        """
        all_instances = []
        if not arg:
            for _, v in storage.all().items():
                all_instances.append(str(v))
        else:
            if arg not in all_class_names:
                print("** class doesn't exist **")
                return False
            for k, v in storage.all().items():
                if k.startswith(f"{arg}."):
                    all_instances.append(str(v))
        print(all_instances)
        return False

    def do_update(self, arg):
        """update : update [CLASS] [ID] [ATTRIBUTE-NAME] [ATTRIBUTE-VALUE]
        CLASS : class name of object to update
        ID : id of class name
        ATTRIBUTE-NAME : attribute to update
        ATTRIBUTE-VALUE : value to set attribute to

        SYNOPSIS : updates an instance based on the class name and id by
                    adding or updating attribute

        EXAMPLE : update User 1234-1234-1234 email "aibnb@mail.com"
        """
        args = parse_arg(arg)
        if len(args) < 4:
            match len(args):
                case 0:
                    print("** class name missing **")
                case 1:
                    print("** instance id missing **")
                case 2:
                    print("** attribute name missing **")
                case 3:
                    print("** value missing **")
        else:
            value = None
            if args[0] == "Place":
                match args[2]:
                    case ("number_rooms" | "number_bathrooms" | "max_guest" |
                            "price_by_night"):
                        value = int(args[3])
                    case "latitude" | "longitude":
                        value = float(args[3])
                    case _:
                        value = args[3]
            else:
                value = args[3]
            setattr(storage.all()[f"{args[0]}.{args[1]}"], args[2],
                    value)
            storage.save()

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


def create_user():
    """Dispatch function called when create is supplied with User argument
    at the command interpreter
    """
    new_user = User()
    new_user.save()
    print(new_user.id)


def create_state():
    """Dispatch function called when create is supplied with State argument
    at the command interpreter
    """
    new_state = State()
    new_state.save()
    print(new_state.id)


def create_city():
    """Dispatch function called when create is supplied with City argument
    at the command interpreter
    """
    new_city = City()
    new_city.save()
    print(new_city.id)


def create_amenity():
    """Dispatch function called when create is supplied with Amenity argument
    at the command interpreter
    """
    new_amenity = Amenity()
    new_amenity.save()
    print(new_amenity.id)


def create_place():
    """Dispatch function called when create is supplied with Place argument
    at the command interpreter
    """
    new_place = Place()
    new_place.save()
    print(new_place.id)


def create_review():
    """Dispatch function called when create is supplied with Review argument
    at the command interpreter
    """
    new_review = Review()
    new_review.save()
    print(new_review.id)


def parse_arg(arg: str) -> list:
    """The command interpreter argument parser

    Args:
        arg: string read from command interpreter to be parsed

    Return:
        Array of parsed arguments
    """
    args = []
    while True:
        first = arg.find('"')
        second = arg[first + 1:].find('"')
        second = second if second == -1 else second + first + 1
        # if no word in between double quotes
        if first == -1 or second == -1:
            args.extend(arg.split())
            break
        else:
            try:
                # if double quotes is placed correctly in the string
                if arg[first - 1] == " ":
                    args.extend(arg[0:first].split())
                    args.extend([arg[first:second + 1]])
                else:
                    args.extend(arg[0:second + 1].split())
            # if double quote falls at the beginning of the string
            # (placed correctly)
            except IndexError:
                args.extend(arg[0:first].split())
                args.extend([arg[first:second + 1]])
        arg = arg[second + 1:]
    return [x.replace('"', "") for x in args]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
    # HBNBCommand().
    # onecmd("update BaseModel 0bfa6496-8f40-4680-abaf-7c9cd3631094
    #  name \"Betty Holberton\"")
    # HBNBCommand().
    # onecmd("show BaseModel 0bfa6496-8f40-4680-abaf-7c9cd3631094")
