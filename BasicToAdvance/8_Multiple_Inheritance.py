"""What is Multiple Inheritance?

Multiple Inheritance means:

A class can inherit features (attributes + methods) from more than one parent class.

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

Child class gets access to everything from both parents.

How Multiple Inheritance Works? 
Child class automatically gets access to:
Parent1 methods
Parent2 methods
Parent1 variables
Parent2 variables
Parent1 constructor (if not overridden)
Parent2 constructor (if not overridden)
Child class can:
Use parent behaviors
Extend parent behaviors
Override parent behaviors   


"""

class A:
    def feature1(self):
        print("Feature 1 from A")

class B:
    def feature2(self):
        print("Feature 2 from B")

class C(A, B):
    def feature3(self):
        print("Feature 3 from C")

obj = C()
obj.feature1()
obj.feature2()
obj.feature3()

# output:
# Feature 1 from A      
# Feature 2 from B
# Feature 3 from C

class A:
    def feature1(self):
        print("Feature 1 from A")

class B:
    def feature1(self):
        print("Feature 1 from B")

class C(A, B):
    pass

obj = C()
obj.feature1()
# output:       
# Feature 1 from A


"""Important Interview Questions & Answers
1. What is multiple inheritance?

A child class inherits from more than one parent class.

2. Does Python support multiple inheritance?

Yes. Unlike Java, Python supports true multiple inheritance.

3. What is the Diamond Problem?

Ambiguity when two parent classes inherit from the same grandparent.
Solved using MRO.

4. What is MRO?

Method Resolution Order — The order in which Python searches for a method.

5. What is super() in multiple inheritance?

super() follows MRO, not just the immediate parent."""  
