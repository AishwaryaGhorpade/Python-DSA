"""What is a Static Variable in Python?

A static variable in Python is also called a class variable.

It is a variable that:

Belongs to the class

Is shared by all objects

Has only one copy in memory

Is accessed using the class name

Static variables are defined inside the class but outside any method.

⭐ Syntax
class ClassName:
    static_var = value   # static / class variable"""

# ⭐ Example 1: Simple Static Variable
class Student:
    school = "Oxford Public School"   # static variable
    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student()
s2 = Student()

print(s1.school)    # Oxford Public School
print(s2.school)    # Oxford Public School
print(Student.school) # Oxford Public School


"""What is a Static Method in Python?

A static method is a method inside a class that does NOT need access to instance (self) or class (cls).

It behaves like a normal function, but it is placed inside a class for logical grouping.

We create a static method using:

@staticmethod

⭐ Why Use Static Methods?

Static methods are used when:

✔ The function is related to the class
✔ But it does NOT need object data
✔ And does NOT modify class data

They act like utility/helper functions inside a class."""

# ✔ Syntax
# class ClassName:
#     @staticmethod
#     def method_name(parameters):
        # code

"""✔ Calling a static method

Using class name → preferred

Using object → allowed but not common"""

# 🌟 Example 1: Simple Static Method
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 10))   # Called using class
# Output: 15


# ✔ No self
# ✔ No cls
# ✔ Works like a normal function

# 🌟 Example 2: Calling Static Method Through Object
class Test:
    @staticmethod
    def greet():
        print("Hello!")

obj = Test()
obj.greet()     # Works
Test.greet()    # Also works

# Output:
# Hello!    
# Both calls are valid, but using class name is preferred.

# 🌟 Example 3: Static Method Used for Validation

# Static methods are widely used in input validation.

class Validator:
    @staticmethod
    def is_valid_age(age):
        return age >= 18

print(Validator.is_valid_age(21))  # True

# 🌟 Example 4: Static Method Used for Formatting
class Formatter:
    @staticmethod
    def format_name(name):
        return name.strip().title()

print(Formatter.format_name("  aISHWARYA  "))  # Aishwarya

# 🌟 Example 5: Using Static Method Inside Another Method
class Shopping:
    
    @staticmethod
    def calculate_discount(amount):
        return amount * 0.10
    
    def final_price(self, amount):
        discount = Shopping.calculate_discount(amount)
        return amount - discount

shop = Shopping()
print(shop.final_price(1000))  # 900

# 🌟 Example 6: Static Method as a Helper for Class
class Temperature:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

print(Temperature.c_to_f(30))  # 86°F

# 🌟 Example 7: With Classmethod + Staticmethod Together
class Demo:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def info():
        print("This is a static method")

Demo.increment()
Demo.info()
print(Demo.count)  # 1

# Output:
# This is a static method
# 1 


# ✔ @classmethod uses cls
# ✔ @staticmethod uses neither

# 🌟 Example 8: Static Method Used for Pure Utility Logic
class Utils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(Utils.is_even(4))  # True

# 🌟 Example 9: Multiple Static Methods in Same Class
class Math:
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return a * b
    @staticmethod
    def div(a, b): return a / b

print(Math.mul(4, 3))  # 12

# 🌟 Example 10: Using Static Method in Real Project (JSON processing)
import json

class JSONHandler:
    
    @staticmethod
    def to_json(data):
        return json.dumps(data)

    @staticmethod
    def from_json(json_string):
        return json.loads(json_string)

data = {"name": "Aishwarya", "age": 24}

js = JSONHandler.to_json(data)
print(js)

print(JSONHandler.from_json(js))

# Output:
# {"name": "Aishwarya", "age": 24}

"""⭐ Where NOT to Use Static Methods

❌ When the method needs self
❌ When the method needs access to class variables (cls)
❌ When the logic depends on object state

Final Key Points

Static methods are just normal functions inside a class.

Used for utility tasks, validation, formatting, calculation, etc.

They do NOT depend on:

object (self)

class (cls)"""