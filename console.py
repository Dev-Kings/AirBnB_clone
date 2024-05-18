#!/usr/bin/python3

import shlex
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

storage = FileStorage()
# storage.reload()


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter for HBNB projects.

    Attributes:
        prompt (str): Command prompt.
        classes (dict): Dictonary of available classes.
    """

    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Command argument.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D).
        Args:
            arg (str): Command argument.

        Returns:
            bool: True to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to
        JSON file.

        Usage: create <class name>

        Args:
            arg (str): Class name.

        Returns:
            None
        """
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
        """
        Print the string representation of an instance.

        Usage: show <class name> <id>

        Args:
            arg (str): Command arguments.

        Returns:
            None
        """
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
        """
        Delete an instance based on class name and id.

        Usage: destroy <class name> <id>

        Args:
            arg (str): Command arguments.

        Returns:
            None
        """
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
        """
        Print all string representations of instances.

        Usage: all or all <class name>

        Args:
            arg (str): Command argument.

        Returns:
            None
        """
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
        """
        Update an instance based on class name and id.

        Usage: update <class name> <id> <attribute name>
        <attribute value>

        Args:
            arg (str): Command arguments.

        Returns:
            None
        """
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

    def default(self, line):
        """
        Called on input line when the command is not recognized
        Args:
            line (str): The command line input.

        Returns:
            None
        """
        args = line.split('.')
        if len(args) == 2:
            class_name, command = args
            command_args = command.split('(')
            command_name = command_args[0]
            if len(command_args) > 1:
                command_params = command_args[1].replace(')', '').split(',')
                command_params = []
                for param in command_params_str.split(','):
                    stripped_param = param.strip()
                    stripped_param = stripped_param.replace('"', '')
                    stripped_param = stripped_param.replace("'", "")
                    command_params.append(stripped_param)
            else:
                command_params = []

            if command_name == 'all':
                self.handle_all(class_name)
            elif command_name == 'count':
                self.handle_count(class_name)
            elif command_name == 'show':
                self.handle_show(class_name, command_params)
            elif command_name == 'destroy':
                self.handle_destroy(class_name, command_params)
            elif command_name == 'update':
                if (
                        len(command_params) == 2 and
                        command_params[1].startswith('{') and
                        command_params[1].endswith('}')
                ):
                    self.handle_update_dict(class_name, command_params)
                else:
                    self.handle_update(class_name, command_params)
            else:
                print("** Unknown sntax: {}".format(line))
        else:
            print("** Unknown suntax: {}".format(line))

    def handle_all(self, class_name):
        """
        Handle the <class name>.all() command to print all
        instances of a class

        Args:
            class_name (str): The class name.

        Returns:
            None
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_instances = storage.all()
        result = []
        for key, obj in all_instances.items():
            if key.split('.')[0] == class_name:
                result.append(str(obj))
        print(result)

    def handle_count(self, class_name):
        """
        Handle the <class name>.count() command to count
        all istances of a class

        Args:
            class_name (str): The class name.

        Returns:
            None
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_instances = storage.all()
        count = 0
        for key in all_instances:
            if key.split('.')[0] == class_name:
                count += 1
        print(count)

    def handle_show(self, class_name, params):
        """
        Handle the <class name>.show(<id>) command to
        print an instane based on its ID.

        Args:
            class_name (str): The class name.
            params (list): List of command parameters.

        Returns:
            None
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(params) < 1:
            print("** instance id missing **")
            return
        instance_id = params[0]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def handle_destroy(self, class_name, params):
        """
        Handle the <class name>.destroy(<id>) command
        to delete an instance based on its ID.

        Args:
            class_name (str): The class name.
            params (list): List of command parameters.

        Returns:
            None
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(params) < 1:
            print("** instance id missing **")
            return
        instance_id = params[0]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def handle_update(self, class_name, params):
        """
        Handle the <class name>.update(
        <id>, <attribute name>,<attribute value>) command.

        Args:
            class_name (str): The class name.
            params (list): The list of parameters.
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(params) < 3:
            print("** attribute name or value missing **")
            return
        instance_id = params[0]
        attribute_name = params[1]
        attribute_value = params[2]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def handle_update_dict(self, class_name, params):
        """
        Handle the <class name>.update(
        <id>, <dictionary representation>)command.

        Args:
            class_name (str): The class name.
            params (list): The list of parameters.
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(params) < 2:
            print("** instance id or dictionary representation missing **")
            return
        instance_id = params[0]
        try:
            attribute_dict = json.loads(params[1].replace("'", '"'))
        except json.JSONDecodeError:
            print("** invalid dictionary representation **")
            return
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        instance = all_instances[key]
        for attr, val in attribute_dict.items():
            setattr(instance, attr, val)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
