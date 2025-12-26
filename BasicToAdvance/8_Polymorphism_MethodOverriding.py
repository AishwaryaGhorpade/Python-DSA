"""What is Method Overriding?

Method Overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.

In simple words:

Same method name, same parameters, different definition.
Child class overrides (replaces) parent class behavior.

Method overriding is used to achieve runtime polymorphism.

🔹 Why Method Overriding is Needed?

Because different child classes need different behaviors for the same method.

Example:

All animals have sound()

But dog, cat, cow produce different sounds

Parent defines the method, child customizes it."""

# 🔥 Basic Example of Method Overriding
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Calling overridden methods:
a = Animal()
d = Dog()
c = Cat()

a.sound()   # Some generic animal sound
d.sound()   # Bark
c.sound()   # Meow


# Same method name → Different output based on object → Polymorphism.

# 🔹 Overriding with Inheritance (Key Requirement)

# Method overriding requires inheritance.

# Child class must inherit from a parent class.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):  # overriding
        print("Child method")
# Calling methods
p = Parent()
c = Child()         
p.show()   # Parent method
c.show()   # Child method   


# 🔥 Calling Parent Class Method from Child Class

# Sometimes you want to use both parent and child versions.

# Use super().

class Parent:
    def display(self):
        print("Parent display")

class Child(Parent):
    def display(self):
        super().display()   # call parent version
        print("Child display")
c = Child()
c.display()    

# Output:
# Parent display
# Child display

"""🔹 Rules for Method Overriding
Rule	Explanation
1	Parent and child methods must have same name
2	Same number of parameters
3	Should use inheritance
4	Child method replaces parent method
5	Optionally call parent method using super()

🔥 Method Overriding vs Method Overloading
| Overriding                   | Overloading                            |
| ---------------------------- | -------------------------------------- |
| Runtime polymorphism         | Compile-time (not native in Python)    |
| Child modifies parent method | Same method name with different params |
| Requires inheritance         | No inheritance required                |
| Same signature               | Different signature                    |"""

# 🔥 Real-life Example for method overring: Payment System

class Payment:
    def make_payment(self):
        print("Making payment")

class CreditCard(Payment):
    def make_payment(self):
        print("Processing credit card payment")

class UPI(Payment):
    def make_payment(self):
        print("Processing UPI payment")
p = Payment()
p.make_payment()

c = CreditCard()
c.make_payment()

u = UPI()
u.make_payment()


# Output:
# Making payment
# Processing credit card payment
# Processing UPI payment

# 🔹 Overriding __str__() in classes

# Used to customize object printing:

class Car:
    def __str__(self):
        return "This is a Car object"

print(Car())
# Output: This is a Car object

# 🔹 Runtime Polymorphism Example
def show_sound(animal):
    animal.sound()   # which method? depends on object at runtime

for obj in [Dog(), Cat()]:
    show_sound(obj)
# Output:
# Bark
# Meow


"""This is runtime polymorphism—Python decides which method to run at runtime.

🔹 When to Use Method Overriding?

When parent method is too generic

When child needs different behavior

When implementing frameworks

When defining base class templates

When working with inheritance-based designs

⭐ Final Summary
Method Overriding happens when:

✔ Child class has same method name as parent
✔ Child implements its own version
✔ Parent method gets replaced in child
✔ Achieves runtime polymorphism
✔ Allows flexible, extensible OOP design

Key tools used:

super()

Inheritance"""