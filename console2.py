#!/usr/bin/python3


"""
Console For AirBnb Clone
"""
import cmd
from models import BaseModel, User, Amenity, Review, City, Place, State
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
        """
        pass

    @staticmethod
    def check_for_braces(command):
        try:
            first_brace = command.index("{")
            second_brace = command.index("}")
            if command[second_brace + 1] == ")":
                return first_brace, second_brace
            else:
                return False, False
        except ValueError:
            return False, False

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
        first_brace, second_brace = self.check_for_braces(line)
        if first_brace is not False:
            core_string = line[:first_brace]
            str_dict = line[first_brace: second_brace + 1]
            dict_args = eval(str_dict)
            for key, val in dict_args.items():
                command = core_string + repr(key) + ', ' + repr(val) + ')'
                self.default(command)
            return
        try:
            functionName = line.split("(")[0].split(".")[1]
            if functionName:
                if inspect.isclass(eval("Place")) is True:
                    # arg = args[0] + ' ' + args[2]
                    if functionName == "all":
                        return self.do_all(args[0])
                    elif functionName == "show":
                        return self.do_show(arg)
                    elif functionName == "destroy":
                        print("in default")
                        print(arg)
                        return self.do_destroy(arg)
                    elif functionName == "update":
                        return self.do_update(line)
                    elif functionName == "count":
                        i = 0
                        object_container = storage.all()
                        for args[0] in object_container:
                            i += 1
                        print(i)
                    else:
                        print("cant found methode: {}".format(functionName))
                        return
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        except Exception as ex:
            raise ex

    def do_create(self, arg):
        """
        Creates a new instance of Airbnb models
        Usage: Create <ClassName>
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                args = str(arg).lstrip().split()
                class_name = args[0]
                new_inst = eval("{}()".format(class_name))
                new_inst.save()
                print(new_inst.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id
        Usage: show <Class_Name> <obj_id>
        """
        args = arg.strip().split()
        class_name = args[0]
        class_id = args[1]
        length = len(args)
        if length == 0:
            print("** class name missing **")
            return
        try:
            eval(class_name)
        except Exception:
            print("** class doesn't exist **")
            return
        if length == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = class_name + "." + class_id
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

        args = arg.strip().split()
        class_name = args[0]
        class_id = args[1]
        length = len(args)

        if length == 0:
            print("** class name missing **")
            return
        try:
            eval(class_name)
        except Exception:
            print("** class doesn't exist **")
            return
        if length == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = class_name + "." + class_id
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

        length = len(args)
        list_strings = []
        if length == 0:
            for obj_id, obj in container_obj.items():
                list_strings.append(str(obj))
            print(list_strings)
            return
        if length == 1:
            class_name = args[0]
            try:
                for obj_id, obj in container_obj.items():
                    if type(obj) is eval(class_name):
                        # the solution is using reper() => print the type too
                        # str(container_obj[obj]) => is a string
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
        try:
            eval(arg)
        except Exception as ex:
            type_error = type(ex).__name__
            print(ex)
            if type_error is SyntaxError:
                print("syntax errer we can return safely")
                return
            elif type_error is NameError:
                print("cant found Class name")
                return

    @staticmethod
    def check_classs_name(obj):
        try:
            eval(obj)
            return True
        except Exception:
            print("** class doesn't exist **")
            exit(0)

    @staticmethod
    def chech_for_id(obj):
        key_id = obj.__class__.__name__ + '.' + obj.id
        try:
            all_objs = storage.all()
            eval(all_objs[key_id])
            return True
        except Exception:
            print("** no instance found **")
            return False

    @staticmethod
    def same_type_as_attr(new_att, att_type):
        try:
            # try to cast
            if att_type is list:
                try:
                    cast_list = eval(new_att)
                    for el in cast_list:
                        print("type el", type(el))
                        if type(el) is not str:
                            print("this is not a string list")
                            return False
                    return cast_list
                except SyntaxError:
                    print("this is not a list")
                    return False
            value = att_type(new_att)
            if att_type is int or att_type is float:
                if value < 0:
                    return False
            return True
        except ValueError:
            # if cast fail return False
            return False

    @staticmethod
    def convert_new_val(obj_new_val):
        """
            if new Value is int or float cast it before setting it
        """
        try:
            if obj_new_val.isdigit():
                return int(obj_new_val)
            elif obj_new_val.replace(".", "").isdigit():
                return float(obj_new_val)
            elif type(eval(obj_new_val)) is list:
                return list(eval(obj_new_val))
            else:
                return obj_new_val
        except Exception:
            return obj_new_val


if __name__ == "__main__":
    HBNBCommand().cmdloop()
