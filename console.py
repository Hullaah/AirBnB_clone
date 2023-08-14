#!/usr/bin/python3
'''
Console file for the airbnb console project for ALX SE curriculum
This is the main entry point for the console
Defines different methods to enable the user perform commands
'''


import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The main AirBnB console class
    """
    prompt = "(hbnb) "
    __MODELS = storage.models()
    __attributes = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    # Commands - these define the console functionality
    def do_EOF(self, _):
        """
        Defines EOF action
        """
        print()
        return True

    def do_quit(self, _):
        """
        Defines the quit command
        """
        return True

    def do_create(self, line):
        """
        Defines the create command for the console
        """
        args = self.parse_arg(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__MODELS.keys():
            print("** class doesn't exist **")
        else:
            new_model = self.__MODELS[args[0]]()
            print(new_model.id)
            new_model.save()

    def do_show(self, line):
        """
        Defines the show command for the console
        """
        args = self.parse_arg(line)
        model_tuple = self.validity_check(args)
        if model_tuple[0] is False:
            print(model_tuple[1])
            return False
        print(storage.all()[model_tuple[1]])

    def do_destroy(self, line):
        """
        Defines the destroy command for the console
        """
        args = self.parse_arg(line)
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
        args = self.parse_arg(line)
        storage.reload()
        if len(args) == 0:
            print([str(model) for model in storage.all().values()])
        elif args[0] not in self.__MODELS.keys():
            print("** class doesn't exist **")
        else:
            print([str(model) for key, model in
                   storage.all().items() if args[0] in key])

    def do_update(self, line):
        """
        Implements the update command for the console
        """
        args = self.parse_arg(line)
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
        new_value = None
        if args[2] in self.__attributes.keys():
            new_value = self.__attributes[args[2]](args[3])
        else:
            new_value = args[3]
        updated_obj = storage.all()[f"{model_tuple[1]}"]
        setattr(updated_obj, args[2], new_value)
        updated_obj.save()

    def count(self, cls):
        """Default method called
        """
        print(len([x for x in storage.all().keys()
                   if x.startswith(cls[:-1])]))

    def arbitrary_update(self, cls: str, line: str, arg: str):
        """This is the dispatch method handler for arbitrary update
        commands
        """
        arr = line.split(",", maxsplit=1)
        if len(arr) == 1:
            return self.do_update(cls + " " + arr[0])
        arr[1] = arr[1].strip()
        first, last = arr[1].find("{"), arr[1].rfind("}")
        if first == -1 and last == -1:
            attr = arr[1].split(",")
            self.do_update(cls + " " + arr[0] + " " + " ".join(attr))
        elif first == 0 and last == len(arr[1]) - 1:
            attr = arr[1][1:last].split(",")
            for x in attr:
                x = x.strip()
                colon = x.find(":")
                self.do_update(" ".join([cls, arr[0], x[:colon], x[colon + 1:]]
                                        ))
        else:
            return super().default(arg)

    def default(self, line):
        """The default method called when the command is not recognised
        """
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.count,
        }
        args = tuple(line.split(".", maxsplit=1))
        if len(args) != 2:
            return super().default(line)
        first, last = args[1].find("("), args[1].rfind(")")
        if first == -1 or last == -1 or last != len(args[1]) - 1:
            return super().default(line)
        try:
            return (methods[args[1][:first]]
                    (args[0] + " " + args[1][first + 1:last]))
        except KeyError:
            if args[1][:first] == "update":
                self.arbitrary_update(args[0], args[1][first + 1:last], line)
            else:
                super().default(line)

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
        print("To show only models of a particular type:")
        print("Usage: all [MODEL_TYPE]")

    def help_update(self):
        """
        Defines help for the update command
        """
        print("Updates an attribute of a model instance")
        print('Usage: update [MODEL_TYPE] [ID] [ATTRIBUTE] "[NEW_VALUE]"')

    # Base functionality for the console
    def emptyline(self):
        """
        Overrides default behaviour for an empty line to not do anything
        """
        pass

    def parse_arg(self, arg: str) -> tuple:
        """parses the arguments into a tuple
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
        return tuple([x.strip('"') for x in args])

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
        if model_key not in storage.all().keys():
            return False, "** no instance found **"
        return True, model_key


if __name__ == "__main__":
    HBNBCommand().cmdloop()
