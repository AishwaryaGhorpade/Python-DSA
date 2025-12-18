"""What Are Access Modifiers in Python?

Access modifiers are rules that decide how and where class attributes (variables) and methods can be accessed.

Python provides three levels of access:

✔ Public
✔ Protected
✔ Private

Unlike Java/C++, Python does not strictly enforce access control.
Instead, it uses naming conventions to indicate the level of access.

Let’s understand each in detail."""

# ⭐ 1. Public Access Modifier (No Underscore)
# ✔ Everything is accessible everywhere
# ✔ Most commonly used

# Example:

from os import access


class Student:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public

s = Student("Aishwarya", 24)
print(s.name)   # Allowed
print(s.age)    # Allowed

#output:
# Aishwarya
# 24

"""Characteristics of Public

Accessible from inside the class

Accessible from outside the class

Accessible from subclasses

Public = No restriction"""

# ⭐ 2. Protected Access Modifier (_single underscore)

"""Protected members are meant for internal use in:

✔ the class
✔ and its subclasses

They are not recommended to be accessed outside,
but Python does not restrict it."""

# Example:

class Student:
    def __init__(self):
        self._marks = 90   # protected

class Child(Student):
    def show(self):
        print(self._marks)  # allowed in subclass

c = Child()
c.show()
print(c._marks)      # Allowed but NOT recommended
# output:
# 90
# 90    

"""Characteristics of Protected:

Starts with one underscore _var

Can be accessed in subclasses

Not enforced by Python → just a convention

Saying: "Don't touch this unless necessary"

Protected = “Use carefully”"""

# ⭐ 3. Private Access Modifier (__double underscore)

# Private members are not accessible outside the class.

# They use name mangling:

# __variable becomes _ClassName__variable


# Example:

class Student:
    def __init__(self):
        self.__password = "mySecret"   # private

s = Student()
print(s.__password)     # ❌ ERROR


# Output:

# AttributeError: 'Student' object has no attribute '__password'

# Access using Name Mangling (not recommended):
print(s._Student__password)   # Allowed but bad practice

# output:
# mySecret


# ⭐ How Private Members Are Used (Encapsulation)

# Private variables are accessed through getter and setter methods:

class Student:
    def __init__(self):
        self.__grade = "A"

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade in ("A", "B", "C"):
            self.__grade = grade
        else:
            print("Invalid grade!")
s = Student()
print(s.get_grade())
s.set_grade("B")
print(s.get_grade())
s.set_grade("E")   # Invalid grade!

# output:
# A
# B
# Invalid grade!   
 
"""Characteristics of Private:
Private = Fully hidden + Controlled access

⭐ Summary Table of Access Modifiers
Modifier	Syntax	Accessible In Class	Accessible in Subclass	Accessible Outside
Public	var	✔ Yes	✔ Yes	✔ Yes
Protected	_var	✔ Yes	✔ Yes	⚠ Yes (not recommended)
Private	__var	✔ Yes	❌ No (except via mangling)	❌ No
🔥 Internal Working of Private Variables (Name Mangling)

Python converts:

__password → _Student__password


This prevents accidental modification."""

# Example:

class A:
    def __init__(self):
        self.__x = 10

a = A()
print(a._A__x)     # 10

# ⭐ Real-Life Example

# Bank Account:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance     # private

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance


# You cannot do:

acc = BankAccount(5000)
acc.__balance = 0   # ❌ does NOT change private balance

# 🔥 Access Modifiers with Methods

# Same rules apply to methods.

# Public method:
def show(): 
    pass

# Protected method:
def _display():
    pass

# Private method:
def __secret():
    pass


"""Private method call inside class:
self.__secret()"""

"""⭐ Important Interview Questions
✔ What are access modifiers in Python?

Public, Protected (_), and Private (__).

✔ Does Python enforce access control?

No, it uses naming conventions (except name mangling for private).

✔ Is _variable really protected?

Not enforced, just a convention.

✔ How do you access private members?

Using getters/setters or name mangling.

✔ Why does Python use name mangling?

To prevent accidental access, not strict hiding.

⭐ Final Summary

Access Modifiers in Python:

✔ Public → accessible anywhere
✔ Protected _var → accessible but meant for internal use
✔ Private __var → hidden using name mangling

Python uses convention over restriction, making the language flexible and developer-friendly."""