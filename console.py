#!/usr/bin/python3
""" console aribnb """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ console airbnb """
    prompt = '(hbnb) '
    file = None
    cls = ['BaseModel', 'User', 'State',
           'City', 'Amenity', 'Place',
           'Review']

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
        elif arg in self.cls:
            instance = eval(arg)()
            instance.save()
            print(f"{instance.id}")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ prints the string representation of an instance """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] in self.cls:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + '.' + args[1]
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
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
            if args[0] in self.cls:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + '.' + args[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """ prints all string represntation of all instances """
        if not arg:
            objVal = []
            for obj in storage.all().values():
                objVal.append(str(obj))
            print(objVal)
        elif arg not in self.cls:
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
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            lenn = len(args)
            if lenn < 2:
                print("** instance id missing **")
            elif lenn < 3:
                print("** attribute name missing **")
            elif lenn < 4:
                print("** value missing **")
            key = args[0] + '.' + args[1]
            if key in storage.all():
                args[3] = args[3].strip('"')
                try:
                    args[3] = int(args[3])
                except Exception:
                    pass
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
