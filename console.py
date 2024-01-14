#!/usr/bin/python3
"""Module contains entry point for command line interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class of the command line interpreter"""
    prompt = '(hbnb)'

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = eval(f"{arg}()")
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        if arg:
            try:
                eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in storage.all().values()
              if not arg or type(obj).__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = arg.split(" ")

        if len(args) < 1:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, args[2], args[3].strip('"'))
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
