#!/usr/bin/env python3

from models.engine.file_storage import FileStorage
storage = FileStorage()
"""
This module contains the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class represents the command interpreter.
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel and saves it to the
        JSON File. """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = arg
            class_to_create = eval(class_name)
            new_instance = class_to_create()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return

        try:
            class_name = args[0]
            class_to_show = eval(class_name)
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            all_objs = storage.all()
            if key in all_objs:
                print(all_onjs[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        saves the change into the JSON file). """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return
        try:
            class_name = args[0]
            class_to_destroy = eval(class_name)
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


    def do_all(self, arg):
        """ Prints all string representation of all instances
        based on the class name. """
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.items()])
            return

        try:
            class_name = eval(arg)
            if(class_name == type(obj)):
                    print([str(obj) for key, obj in all_objs.items()])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating attribute. """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return
        try:
            class_name = args[0]
            class_to_update = eval(class_name)
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            setattr(all_objs[key], attr_name, attr_value)
            storage.save()
        except NameError:
            print("** class doesn't exist **")
            

    

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Override the default behavior for empty line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()  
