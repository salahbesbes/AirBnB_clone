#!/usr/bin/python3
import cmd
from models import BaseModel , User, Amenity, Review, City, Place, State
import inspect
import models
storage = models.storage
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

    def default(self, line):
        """
        """
        try:
            args = (line.replace('(', '.').replace(',', '.').replace(' ', '')
               [:-1].split('.'))
            if len(args) > 1:
                if inspect.isclass(eval(args[0])) is True:
                    arg = args[0] + ' ' + args[2]
                    if args[1] == "all":
                        return self.do_all(args[0])
                    elif args[1] == "show":
                        return self.do_show(arg)
                    elif args[1] == "destroy":
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
                eval(args[0])
                for obj_id in container_obj.keys():
                    if type(container_obj[obj_id]) is eval(args[0]):
                        # the solution is using reper() => print the type too
                        # str(container_obj[obj_id]) => is a string
                        obj = container_obj[obj_id]
                        list_strings.append(str(obj))
                print(list_strings)
            except Exception:
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
        length_args = len(args)
        if length_args == 0:
            print("** class name missing **")
        elif length_args == 1:
            print("** instance id missing **")
        elif length_args == 2:
            print("** attribute name missing **")
        elif length_args == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            obj_attr = args[2]
            obj_new_val = args[3]
            obj_new_val = obj_new_val[1:-1]
            try:
                eval(class_name)
                key_id = class_name + "." + obj_id
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = container_obj[key_id]
                    try:
                        type_attr = type(getattr(obj, obj_attr))
                        if self.same_type_as_attr(obj_new_val, type_attr) is True:
                            obj_new_val = type_attr(obj_new_val)
                        else:
                            return
                    except Exception as ex:
                        print(ex)
                        pass
                    setattr(obj, obj_attr, obj_new_val)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except Exception as ex:
                print(ex)
                print("** class doesn't exist **")

    @staticmethod
    def same_type_as_attr(new_att, att_type):
        try:
            # try to cast
            value = att_type(new_att)
            print(value)
            if att_type is list:
                if len(value[0]) == 1:
                    return False
            if att_type is int or att_type is float:
                if value < 0:
                    return False
            return True
        except ValueError:
            # if cast fail return False
            return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
