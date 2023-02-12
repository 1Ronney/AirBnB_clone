#!/usr/bin/python3
"""
AIRBNB  console
"""
import json
import cmd
import sys
import os.path
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Command line class for A console"""

    prompt = '(hbnb)'

    def do_EOF(self, args):
        """ exit on Ctrl-D and EOF """
        raise SystemExit

    def do_quit(self, args):
        """ Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
