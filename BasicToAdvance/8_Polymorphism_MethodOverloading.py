"""What is Method Overloading?

Method Overloading means:

Multiple methods with the same name but different parameters (type, number, order) inside the same class.

Example in languages like Java:

add(int a, int b)
add(double a, double b)
add(int a, int b, int c)


Same method name → different signatures.

❌ Python Does NOT Support Method Overloading Natively

Python does not support true method overloading because:

Python functions do not consider parameter type or count.

If you define the same method twice, the last one overrides the previous one."""

# Example:

class Example:
    def show(self, a):
        print(a)

    def show(self, a, b):
        print(a, b)

obj = Example()
obj.show(10)


# Output:
# TypeError: show() missing 1 required positional argument


"""Why?
Because the second show() replaced the first one.

🔹 So how do we implement Method Overloading in Python?

Python supports method overloading-like behavior using:4 ways

✔ Default arguments
✔ Variable-length arguments (*args, **kwargs)
✔ Type-checking inside a single method
4. Using Function Overloading with functools.singledispatch"""

# Let’s see each technique.

# ⭐ 1. Using Default Arguments
class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))        # 5
print(m.add(2, 3, 4))     # 9
print(m.add(10))          # 10

# ✔ Works like overloading
# ✔ Same method, multiple behaviors


# ⭐ 2. Using *args (Variable-Length Arguments)
class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(2, 3))            # 5
print(m.add(2, 3, 4))         # 9
print(m.add(1, 2, 3, 4, 5))   # 15

# ✔ Accepts unlimited arguments
# ✔ Behaves differently based on input


# ⭐ 3. Type Checking Inside a Method
class Display:
    def show(self, value):
        if isinstance(value, int):
            print("Integer:", value)
        elif isinstance(value, str):
            print("String:", value)
        else:
            print("Unknown type")
obj = Display()
obj.show(10)        # Integer:10
obj.show("Hi")      # String:Hi

# ✔ Behavior changes based on type
# ✔ Emulates method overloading


# ⭐ 4. Using Function Overloading with functools.singledispatch

# Python supports function overloading, not method overloading.

from functools import singledispatch

@singledispatch
def fun(arg):
    print("Default:", arg)

@fun.register(int)
def _(arg):
    print("Integer:", arg)

@fun.register(str)
def _(arg):
    print("String:", arg)

fun(10)        # Integer 10
fun("Hi")      # String Hi
fun(10.5)      # Default 10.5

"""✔ True function-based overloading
✔ Works by type
❌ Not directly inside classes
🔹 Why Python Avoided True Method Overloading?

Because Python is dynamic, not static:

You can pass any type anytime

Functions can handle any number of arguments

The language design encourages simplicity via *args and default parameters

So Python avoids the complexity of overloaded signatures."""

# 🔥 Real-Life Example: Overloading area() Method
class Area:
    def calculate(self, *args):
        if len(args) == 1:
            r = args[0]
            print("Area of Circle:", 3.14 * r * r)
        elif len(args) == 2:
            l, b = args[0], args[1]
            print("Area of Rectangle:", l * b)
        else:
            print("Invalid input")

a = Area()
a.calculate(5)
a.calculate(10, 20)

# 🔥 Real-Life Example: Calculator
class Calculator:
    def operate(self, a, b=None):
        if b is None:
            print("Square:", a * a)
        else:
            print("Sum:", a + b)

c = Calculator()
c.operate(5)      # Square 25
c.operate(5, 3)   # Sum 8

# 🔹 Method Overloading vs Method Overriding
"""| Overloading                            | Overriding                          |
| -------------------------------------- | ----------------------------------- |
| Same method name, different parameters | Same method name & parameters       |
| Happens in the **same class**          | Happens in **parent-child classes** |
| Python simulates it                    | Python fully supports it            |
| Compile-time polymorphism              | Runtime polymorphism                |

⭐ Final Summary
✔ Python does NOT support traditional method overloading
✔ Overloading is achieved using:

Default parameters

*args and **kwargs

Type checking

singledispatch (function overloading)

✔ Overloading = Compile-time polymorphism
✔ Overriding = Runtime polymorphism"""