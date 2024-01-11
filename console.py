#!/usr/bin/python3
"""
console: this module contains the code
for the command line interpreter
"""

import cmd
from models.base_model import BaseModel
import models

classes = {
    "BaseModel": BaseModel,
}


class HBNBCommand(cmd.Cmd):
    """HBNB CONSOLE"""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create an instance of the Base model,
        save it to a file and print its id.
        """

        args = arg.split()
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

        args = arg.split()
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

    def do_destroy(self, arg):
        """Deletes an instance."""

        args = arg.split()
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

        args = arg.split()
        ins_obj = []

        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return False
        for key, value in models.storage.all().items():
            if len(args) == 0 or key.startswith(args[0]):
                ins_obj.append(str(value))
        print(ins_obj)

    def do_quit(self, arg):
        """Exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program."""

        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
