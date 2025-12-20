"""Class Method in Python – Detailed Explanation

A class method is a method that is bound to the class, not to an object (instance).
It is mainly used to access or modify class-level data (class variables).

1️⃣ What is a Class Method?

A class method:

Uses the decorator @classmethod

Takes cls as its first parameter

Works on class variables

Can be called using class name or object

Syntax
class ClassName:
    @classmethod
    def method_name(cls, arguments):
        # class-level logic"""

# 2️⃣ Basic Example
class Demo:
    count = 0   # class variable

    @classmethod
    def increase(cls):
        cls.count += 1
        return cls.count

print(Demo.increase())  # 1
print(Demo.increase())  # 2

# 🔍 Explanation

# cls → refers to the class Demo

# cls.count → accesses class variable

# Value is shared among all objects

# 3️⃣ Calling Class Method Using Object
obj = Demo()
print(obj.increase())  # 3


# ✔ Still modifies the same class variable

# 4️⃣ Why Class Method is Needed?
# ❌ Problem with instance method
class Student:
    college = "ABC College"

    def change_college(self):
        self.college = "XYZ College"

s1 = Student()
s1.change_college()

print(Student.college)  # ABC College ❌ not changed

# ✅ Solution using class method
class Student:
    college = "ABC College"

    @classmethod
    def change_college(cls):
        cls.college = "XYZ College"

Student.change_college()
print(Student.college)  # XYZ College ✅

# 5️⃣ Class Method vs Static Method
# 1. Static Method ❌ (no access to class data)
class Test:
    count = 0

    @staticmethod
    def increase():
        Test.count += 1

# 2. Class Method ✅ (clean and recommended)
class Test:
    count = 0

    @classmethod
    def increase(cls):
        cls.count += 1
"""
# | Feature                | Class Method   | Static Method        |
| ---------------------- | -------------- | -------------------- |
| Decorator              | `@classmethod` | `@staticmethod`      |
| First parameter        | `cls`          | No default parameter |
| Access class variables | ✅ Yes          | ❌ No (directly)      |
| Modify class data      | ✅ Yes          | ❌ Not naturally      |.  """



# 6️⃣ Factory Method (Very Important Use Case ⭐)
    # -Class methods are commonly used as factory methods.
# Example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        name, marks = data.split(",")
        return cls(name, int(marks))

s1 = Student.from_string("Aishwarya,90")
print(s1.name, s1.marks)    # Aishwarya 90


# ✔ Creates object in an alternative way

# 7️⃣ Accessing Class Variables Across Inheritance
class Parent:
    value = 10
    @classmethod
    def show(cls):
        print(cls.value)

class Child(Parent):
    value = 20

Child.show()  # 20

# 🔑 Why?
# cls refers to the calling class
# Supports polymorphism

# 8️⃣ Difference: Instance Method vs Class Method
class Sample:
    x = 10

    def instance_method(self):
        print(self.x)

    @classmethod
    def class_method(cls):
        print(cls.x)
obj = Sample()
obj.instance_method()  # 10 ✔ Access via instance
Sample.class_method()  # 10 ✔ Access via class 



"""
| Method          | Access                  |
| --------------- | ----------------------- |
| Instance Method | Instance + Class        |
| Class Method    | Class only              |
| Static Method   | Neither (unless forced) |

9️⃣ When Should You Use Class Methods?

✅ Use class methods when:

Working with class-level data

Creating alternative constructors

Writing logic common to all objects

Supporting inheritance & polymorphism

❌ Don’t use class methods for:

Object-specific behavior

Instance data processing

🔟 One-Line Definition (Exam Ready)

A class method is a method that operates on the class rather than an instance and is used to access or modify class-level data using the cls parameter."""