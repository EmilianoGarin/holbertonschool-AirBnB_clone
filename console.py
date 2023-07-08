#!/usr/bin/python3
""" console aribnb """
import cmd
from models.base_model import BaseModel
from models import storage


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
            instance.save()
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
                key = args[0] + '.' + args[1]
                objects = storage.all()
                if key in objects:
                    print(f"{objects[key]}")
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ deletes an instance based on the class and id """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] == "BaseModel":
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + '.' + args[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """ prints all string represntation of all instances """
        if not arg:
            objVal = []
            for obj in storage.all().values():
                objVal.append(str(obj))
            print(objVal)
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            objVal = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    objVal.append(str(obj))
            print(objVal)

    def do_update(self, arg):
        """ updates an instance based on class and id """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            lenn = len(args)
            if lenn == 1:
                print("** instance id missing **")
            elif lenn == 2:
                print("** attribute name missing **")
            elif lenn == 3:
                print("** value missing **")
            key = args[0] + '.' + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
