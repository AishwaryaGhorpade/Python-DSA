# The super() keyword is used to call methods or access variables of a parent (base) class from a child (derived) class.

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()   # calling parent method
        print("This is Child class")

c = Child()
c.show()

# Output:
# This is Parent class
# This is Child class   


class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized")

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # calls Person constructor
        self.salary = salary
        print("Employee initialized")

e = Employee("Aishwarya", 50000)
print(e.name)    # Aishwarya
print(e.salary)  # 50000    

# Output:
# Person initialized
# Employee initialized  
# Aishwarya
# 50000
