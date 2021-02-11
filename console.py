import cmd
from BaseModel import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    # ----- basic turtle commands -----
    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        pass





