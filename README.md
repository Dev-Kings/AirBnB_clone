# 0x00. AirBnB clone - The console

## Concepts covered:

- Python packages
- AirBnB clone

### What’s a command interpreter?

It’s exactly like the Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of the project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### A command interpreter to manage AirBnB objects.

This is the first step towards building full web application: the AirBnB clone.

Each task is linked and helps to:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all the classes and the storage engine

### General Milestones Covered

- Creating a Python package
- Creating a command interpreter in Python using the cmd module
- Unit testing and implementation in a large project
- Serializing and deserializing a Class
- Writing and reading a JSON file
- Managing datetime
- UUID
- *args and how to use it
- **kwargs and how to use it
- Handling named arguments in a function

## How to start it

## How to use it

## Examples

## Collaborators
- [Daniel Kipkosgei](https://www.linkedin.com/in/daniel-kipkosgei-2ab84117b/)
- [David King'asia](https://www.linkedin.com/in/davidkingasia/

