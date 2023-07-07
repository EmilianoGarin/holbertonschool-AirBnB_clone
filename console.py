#!/usr/bin/python3
""" console aribnb """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ console airbnb """
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """ empty line """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Quit when reaches end of file """
        return True

    def do_create(self, arg):
        """ creates a new instance """
        if not arg:
            print("** class name missing **")
        if arg == "BaseModel":
            instance = BaseModel()
            print(f"{instance.id}")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ prints the string representation of an instance """
        if not arg:
            print("** class name missing **")
        args = arg.split()
        if args[0] == "BaseModel":
            if len(args) == 1:
                print("** instance id missing **")
            else:
                pass
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ deletes an instance based on the class and id """
        pass

    def do_all(self, arg):
        """ prints all string represntation of all instances """
        pass

    def do_update(self, arg):
        """ updates an instance based on class and id """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
