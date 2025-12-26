# Dunder methods are special methods that allow developers to customize object behavior and enable operator overloading in Python.

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["A", "B", "C"])
print(len(t))  # 3
# Output:
# 3

# Operator Overloading (Very Important ⭐)
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

a = Number(10)
b = Number(20)

print(a + b)   # 30
# Output:
# 30

"""Common Dunder Methods for Operator Overloading:
| Operator | Dunder Method |
| -------- | ------------- |
| `+`      | `__add__`     |
| `-`      | `__sub__`     |
| `*`      | `__mul__`     |
| `/`      | `__truediv__` |
| `//`     | `__floordiv__`|
| `%`      | `__mod__`     |"""


# Comparison Magic Methods
class Person:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

p1 = Person(25)
p2 = Person(18)

print(p1 > p2)  # True
# Output:
# True  

"""| Operator | Method   |
| -------- | -------- |
| `==`     | `__eq__` |
| `>`      | `__gt__` |
| `<`      | `__lt__` |
| `>=`     | `__ge__` |
| `<=`     | `__le__` |
| `!=`     | `__ne__` |"""


# __str__ vs __repr__
class Student:
    def __str__(self):
        return f"Student Name: {self.name}"
    def __repr__(self):
        return f"Student('{self.name}')"    
s = Student()
s.name = "John"
print(s)         #Student Name: John
print(str(s))    # Student Name: John
print(repr(s))   # Student('John')
# Output:
# Student Name: John
# Student Name: John
# Student('John')   
# __str__ is meant for a readable representation, while __repr__ is meant for an unambiguous representation useful for debugging.

# __call__ Dunder Method
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x   
add_five = Adder(5)
result = add_five(10)  # Calls __call__ method
print(result)  # 15
# Output:
# 15
# The __call__ method allows an instance of a class to be called as a function.
# This can be useful for creating callable objects or implementing function-like behavior in classes.

# __new__ vs __init__ (Advanced)
class Demo:
    def __new__(cls):
        print("Object created")
        return super().__new__(cls)

    def __init__(self):
        print("Object initialized")

d = Demo()
# Output:
# Object created
# Object initialized
# __new__ is responsible for creating a new instance of a class, while __init__ initializes the instance after it has been created.
# __new__ is called before __init__ and is rarely overridden unless you need to control the creation of new instances.
# The super() keyword is used to call methods or access variables of a parent (base) class from a child (derived) class.

# __getitem__ & __setitem__ (Indexing)
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

lst = MyList([10, 20, 30])
print(lst[1])   # 20
lst[1] = 50
print(lst[1])   # 50
# Output:
# 20
# 50    
# The __getitem__ and __setitem__ methods allow instances of a class to use indexing syntax (e.g., obj[index]) for getting and setting values, respectively.    
# This is useful for creating custom container types that behave like lists or dictionaries.

# __call__ – Make Object Callable
class Hello:
    def __call__(self):
        print("Object called like function")

h = Hello()
h()   # Object called like function
# Output:
# Object called like function   

"""
Most Common Dunder Methods (Must Remember)
__init__
__str__
__repr__
__add__
__eq__
__len__
__getitem__
__call__"""
