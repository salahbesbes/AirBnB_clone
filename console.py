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
            args = (line.replace('(', '.').replace(',', '.').replace(' ', '')
                    .replace('"', "").replace("'", "")[:-1].split('.'))
            print(args)
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
                        new_command = arg + ' ' + args[3] + ' ' + args[4]
                        return self.do_update(new_command)
                    elif args[1] == "count":
                        i = 0
                        object_container = storage.all()
                        for args[0] in object_container:
                            i += 1
                        print(i)
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        except Exception:
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
            except Exception:
                print("** class doesn't exist **")
                return

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
        except Exception:
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
        except Exception:
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
                except Exception:
                    print("** no instance found **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 2:
            try:
                eval(args[0])
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return

        if len(args) >= 3:
            try:
                eval(args[0])
                if len(args) == 3:
                    print("** value missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 4:
            class_name = args[0]
            obj_id = args[1]
            obj_attr = args[2]
            obj_new_val = args[3]
            try:
                eval(class_name)
                key_id = class_name + "." + obj_id
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = container_obj[key_id]
                    try:
                        type_attr = type(getattr(obj, obj_attr))
                        if self.same_type_as_attr(
                                obj_new_val, type_attr)is not False:
                            obj_new_val = type_attr(obj_new_val)
                        else:
                            return
                    except Exception as ex:
                        a = len(obj_new_val) - 1
                        if ((obj_new_val[0] == "\'") or
                                (obj_new_val[0] == "\"")) and (
                                (obj_new_val[a] == "\'")
                                or (obj_new_val[a] == "\"")):
                            obj_new_val = obj_new_val[1:-1]
                    obj_new_val = self.convert_new_val(obj_new_val)
                    setattr(obj, obj_attr, obj_new_val)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except Exception as ex:
                print("** class doesn't exist **")

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
                            return False
                    return cast_list
                except SyntaxError:
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
