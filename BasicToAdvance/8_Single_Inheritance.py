"""What is Single Inheritance?

Single Inheritance is the simplest and most commonly used form of inheritance.

It means:

A child class inherits from only one parent class.

So there is one parent → one child.

This forms a one-level inheritance hierarchy.

ow Single Inheritance Works?

Child class automatically gets access to:

Parent methods

Parent variables

Parent constructor (if not overridden)

Child class can:

Use parent behavior

Extend parent behavior

Override parent behavior
"""


class parent:
    name="Aishwarya"
    def show_parent(self):
        print("This is parent class method")
class child(parent):
    def show_child(self):
        print("This is child class method")
c = child()
print(c.name)
c.show_parent()
c.show_child()

# output:
# Aishwarya
# This is parent class method
# This is child class method


"""Interview Questions (Most Asked)
✔ What is single inheritance?

A child class inherits from only one parent class.

✔ Does the child class inherit attributes and methods?

Yes, all public and protected members.

✔ Can child override parent methods?

Yes, using overriding.

✔ Can child call parent method?

Yes, using super().

✔ What is MRO?

Method Resolution Order — order in which Python searches for methods."""