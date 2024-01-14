#!/usr/bin/python3
"""Module contains entry point for command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class of the command line interpreter"""
    prompt = '(hbnb)'

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
