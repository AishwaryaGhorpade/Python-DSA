class Parent:
    def __init__(self):
        print("Parent constructor")
class Child1(Parent):
    def __init__(self):
        print("Child1 constructor")
        super().__init__()

class Child2(Parent):
    def __init__(self):
        print("Child2 constructor")
        super().__init__()
c1 = Child1()
c2 = Child2()
# output:
# Child1 constructor
# Parent constructor
# Child2 constructor
# Parent constructor    