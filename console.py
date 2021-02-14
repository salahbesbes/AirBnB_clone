#!/usr/bin/python3


"""
Console For AirBnb Clone
"""
import cmd
from models import BaseModel , User, Amenity, Review, City, Place, State
import inspect
import models
storage = models.storage


class HBNBCommand(cmd.Cmd):
    """
        Console Class
    """
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
        Handle when empty line introduced 
        """
        pass

    def default(self, line):
        """
            Change Default console action:
            Usage:
                <class name>.count()
                <class name>.all()
                <class name>.show(<id>)
                <class name>.destroy(<id>)
                <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        try:
            args = (line.replace('(', '.').replace(',', '.').replace(' ', '').replace('"',"").replace("'","")
               [:-1].split('.'))
            print(args)
            if len(args) > 1:
                if inspect.isclass(eval(args[0])) is True:
                    arg = args[0] + ' ' + args[2]
                    if args[1] == "all":
                        return self.do_all(args[0])
                    elif args[1] == "show":
                        return self.do_show(arg)
                    elif args[1] == "destroy":
                        print("in default")
                        print (arg)
                        return self.do_destroy(arg)
                    elif args[1] == "update":
                        return self.do_update(arg + ' ' + args[3] + ' ' + args[4])
                    elif args[1] == "count":
                        i = 0
                        object_container = storage.all()
                        for args[0] in object_container:
                            i += 1
                        print(i)
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        except:
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
        storage.reload()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) >= 1:
            try:
                eval(args[0])
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                try:
                    key_id = args[0] + "." + args[1]
                    container_obj = storage.all()
                    container_obj[key_id]
                except:
                    print("** no instance found **")
                    return
            except:
                print("** class doesn't exist **")
                return
        if len(args) >= 2:
            try:
                eval(args[0])
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
            except:
                print("** class doesn't exist **")
                return

        if len(args) >= 3:
            try:
                eval(args[0])
                if len(args) == 3:
                    print("** value missing **")
                    return
            except:
                print("** class doesn't exist **")
                return
        if len(args) >= 4:
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
                    if ((value_id[0] == "\'") or (value_id[0] == "\"")) and ((value_id[len(value_id)-1] == "\'") or (value_id[len(value_id)-1] == "\"")):
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
