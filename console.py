#!/usr/bin/python3
"""
console: this module contains the code
for the command line interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models
import shlex

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    """HBNB CONSOLE"""

    prompt = '(hbnb) '

    def default(self, arg):
        """
        Default method of the console.
        This handles special inputs like User.create()
        """
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "create": self.do_create,
            "update": self.do_update,
            "count": self.count
        }
        args = arg.split(".")
        if len(args) != 2:
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        command = args[1].split("(")
        if len(command) < 2:
            return False
        if len(command[1]) == 0:
            return False
        if command[1][-1] != ")":
            return False
        command[1] = command[1][:-1].split(",")
        command[1] = "".join(command[1])
        return methods[command[0]]("{} {}".format(args[0], command[1]))

    def do_create(self, arg):
        """Create an instance of the Base model,
        save it to a file and print its id.
        """

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            base_model = classes[args[0]]()
            base_model.save()
            print(base_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(models.storage.all()[key], args[2], args[3])
                        models.storage.all()[key].save()
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance."""

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""

        args = shlex.split(arg)
        ins_obj = []

        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return False
        for key, value in models.storage.all().items():
            if len(args) == 0 or key.startswith(args[0]):
                ins_obj.append(str(value))
        print(ins_obj)

    def count(self, arg):
        """retrieves the number of instances of a class"""

        ins_obj = []
        args = shlex.split(arg)
        if len(args) < 1 or args[0] not in classes:
            print("** class doesn't exist **")
            return False
        for key, value in models.storage.all().items():
            if key.startswith(args[0]):
                ins_obj.append(str(value))
        print(len(ins_obj))

    def emptyline(self):
        """Handles empty line"""

        return False

    def do_quit(self, arg):
        """Exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program."""

        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
