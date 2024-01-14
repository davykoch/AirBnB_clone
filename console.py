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
        saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = globals()[arg]()
            if not isinstance(obj, BaseModel):
                raise NameError
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")
        except NameError:
            print("** class doesn't inherit from BaseModel **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on class name and id"""
        args = arg.split()
        
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        
        if class_name not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = f"{class_name}.{instance_id}"
        if key not in FileStorage.__objects:
            print("** no instance found **")
            return

        del FileStorage.__objects[key]
        FileStorage().save()

    def do_all(self, arg):
        """Prints all string representations of
        instances, optionally filtered by class name"""
        args = arg.split()

        if len(args) > 0 and args[0] not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
            return

        instances = []
        for key, obj in FileStorage.__objects.items():
            if len(args) == 0 or args[0] == obj.__class__.__name__:
                instances.append(str(obj))

        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute"""
        args = arg.split(" ")

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = f"{class_name}.{instance_id}"
        if key not in FileStorage.__objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if attribute_name in ['id', 'created_at', 'updated_at']:
            return

        instance = FileStorage.__objects[key]
        setattr(instance, attribute_name, attribute_value)
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
