#!/usr/bin/env python3

import shlex
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

storage = FileStorage()
# storage.reload()

class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter for HBNB project.
    """

    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'user' : User,
        # Add other models here
    }
    
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print()
        return True
    
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass
    
    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to 
        JSON file."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if key in all_instances:
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        all_instances = storage.all()
        if not args:
            print([str(all_instances[key]) for key in all_instances])
        else:
            try:
                class_name = args[0]
                print_instances = []
                for key in all_instances:
                    if key.split('.')[0] == class_name:
                        print_instances.append(str(all_instances[key]))
                if print_instances:
                    print(print_instances)
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if key not in all_instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3]
            instance = all_instances[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
