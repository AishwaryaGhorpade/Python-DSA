"""What is Multilevel Inheritance?

Multilevel inheritance means:

A class inherits from a parent class,
and another class inherits from that child class.

This creates a chain (levels) of inheritance.

Structure:

Class A → Class B → Class C


B inherits from A

C inherits from B

Therefore, C indirectly inherits from A

Why Use Multilevel Inheritance?

To create a logical, multi-step hierarchy

To extend features step by step

To reuse code at multiple levels

Useful in hierarchical real-world models
"""

class A:
    def methodA(self):
        print("Method in A")

class B(A):
    def methodB(self):
        print("Method in B")

class C(B):
    def methodC(self):
        print("Method in C")
obj = C()
obj.methodA()   # from A
obj.methodB()   # from B
obj.methodC()   # from C

# output:
# Method in A
# Method in B
# Method in C


# Multilevel Inheritance with Constructor
class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()

class C(B):
    def __init__(self):
        print("C constructor")
        super().__init__()

obj = C()

# output:
# C constructor
# B constructor
# A constructor 

"""Interview Questions (Most Asked)
✔ What is multilevel inheritance?

A chain of inheritance where class C inherits from class B, and class B inherits from class A.

✔ How is multilevel inheritance different from multiple inheritance?

Multilevel: A → B → C

Multiple: C inherits from A and B together

✔ Does Python support multilevel inheritance?

Yes.

✔ How do you call parent class methods?

Using super().

✔ What is the MRO in multilevel inheritance?

Child → Parent → Grandparent."""
