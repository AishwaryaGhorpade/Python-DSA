# Hybrid Inheritance is a combination of two or more types of inheritance.

class A:
    def featureA(self):
        print("Feature from A")
class B(A):
    def featureB(self):
        print("Feature from B")

class C(A):
    def featureC(self):
        print("Feature from C")
class D(B, C):
    def featureD(self):
        print("Feature from D")
obj = D()
obj.featureA()  # from A
obj.featureB()  # from B
obj.featureC()  # from C
obj.featureD()  # from D

# output:
# Feature from A            
# Feature from B
# Feature from C
# Feature from D    

# Hybrid Inheritance with Constructors
class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()

class C(A):
    def __init__(self):
        print("C constructor")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D constructor")
        super().__init__()
obj = D()
# output:
# D constructor
# B constructor         
# C constructor
# A constructor

# Note: The order of constructor calls follows the Method Resolution Order (MRO) in Python.
# In this case, D -> B -> C -> A


"""Important Interview Questions
✔ What is hybrid inheritance?

Combination of two or more types of inheritance.

✔ Does Python support hybrid inheritance?

Yes.

✔ What is MRO?

Order in which Python solves method resolution when multiple parents exist.

✔ How does Python handle diamond problem?

Using C3 Linearization (MRO).

✔ Give a real-life example of hybrid inheritance.

WorkingStudent = Employee + Student, both inherit from Person."""



