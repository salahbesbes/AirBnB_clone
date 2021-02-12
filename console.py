#!/usr/bin/python3
import cmd
from models import BaseModel
from models import FileStorage
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # ----- basic turtle commands -----
    def do_EOF(self, arg):
        """

        """
        'EOF command to exit the program\n'
        return True

    def do_quit(self, arg):
        """
            quit 
        """
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        'Create new instance\n'
        """
            Creates a new instance of Airbnb models
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                args = arg.split()
                # split the args and use eval (evaluate expression dynamically to Python expression) for example :
                # arg [0] = BaseModel it will evaluate to BaseModel() 
                # arg[0] = ahmed it will fail cuz there is no method or any python expretion as ahmed()
                # it will only work with method or module imported in the file source 
                new_inst = eval(args[0])()
                new_inst.save()
                print(new_inst.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        """
        container_obj = []
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        if len (args) == 1:
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
        if len (args) == 1:
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
        """
        storage = FileStorage()
        storage.reload()
        container_obj = storage.all()
        args = arg.split()
        if len(args) == 0:
            for obj_id in container_obj.keys():
                obj = container_obj[obj_id]
                print(obj)
            return
        if len(args) == 1:
            try:
                for obj_id in container_obj.keys():
                    if type(container_obj[obj_id]) is eval(args[0]):
                        print(container_obj[obj_id]) 
            except: 
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """
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
                    try:
                        value = container_obj[key_id]
                        type_atr = type(getattr(value, args[2]))
                        args[3] = type_atr(args[3])
                    except:
                        pass
                    value_id = args[3]
                    value_id = value_id[1:-1]
                    setattr(value, args[2], value_id)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except:
                print("** class doesn't exist **")


HBNBCommand().cmdloop()
