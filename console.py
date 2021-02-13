#!/usr/bin/python3
import cmd
from models import BaseModel , User, Amenity, Review, City, Place, State
from models import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of Airbnb models
        Usage: Create <ClassName>
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                args = arg.split()
                # it will only work with module imported in the file source
                # else raise exception
                new_inst = eval("{}()".format(args[0]))
                new_inst.save()
                print(new_inst.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id
        Usage: show <Class_Name> <obj_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                value = container_obj[key_id]
                print(value)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <Class_Name> <obj_id>
        """

        args = arg.split()
        container_obj = []
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                del container_obj[key_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all <Class_Name>  OR  all
        """
        storage = FileStorage()
        storage.reload()
        container_obj = storage.all()
        args = arg.split()
        list_strings = []
        if len(args) == 0:
            for obj_id in container_obj.keys():
                obj = container_obj[obj_id]
                list_strings.append(str(obj))
            print(list_strings)
            return
        if len(args) == 1:
            try:
                for obj_id in container_obj.keys():
                    if type(container_obj[obj_id]) is eval(args[0]):
                        # the solution is using reper() => print the type too
                        # str(container_obj[obj_id]) => is a string
                        obj = container_obj[obj_id]
                        list_strings.append(str(obj))
                print(list_strings)
            except:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        $ update BaseModel 1234-1234 email "x@g.com" first_name "yy" is equal
        $ update BaseModel 1234-1234 email "x@g.com"
        """
        storage = FileStorage()
        storage.reload()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            try:
                eval(args[0])
                key_id = args[0] + "." + args[1]
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = ""
                    try:
                        obj = container_obj[key_id]
                        type_atr = type(getattr(obj, args[2]))
                        args[3] = type_atr(args[3])
                    except:
                        pass
                    value_id = args[3]
                    value_id = value_id[1:-1]
                    setattr(obj, args[2], value_id)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
