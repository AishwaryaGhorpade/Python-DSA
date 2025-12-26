"""Duck Typing is very easy to implement in Python, because Python focuses on behavior, not type.

Here is a clear, simple explanation with examples so you understand exactly how to implement Duck Typing.

🔹 What is Duck Typing?

Duck Typing means:
It cares only about whether the object has the required method.
If an object has the required method, Python will use it —
regardless of the object's class or type.

Python checks capabilities, not type.

🔥 How to Implement Duck Typing in Python

Duck typing is implemented by:

✔ Writing a function that calls a method
✔ Ensuring different classes implement that method
✔ Passing objects of different classes to the same function

Python won’t care about the class —
it only cares whether the method exists."""


#Basic example of Duck Typing in Python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()   # No type checking!

make_sound(Dog())   # Bark
make_sound(Cat())   # Meow

# output
# Bark
# Meow

#Polymorphism with duck typing
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VSCode:
    def execute(self):
        print("Linting")
        print("Executing code")

class Programmer:
    def code(self, ide):
        ide.execute()

prog = Programmer()
prog.code(Pycharm())
prog.code(VSCode())


# output
# Compiling
# Running
# Linting
# Executing code        


# Here:

# Function name is same

# Behavior changes based on object