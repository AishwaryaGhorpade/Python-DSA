"""Decorators in Python – Complete & Detailed Explanation

A decorator in Python is a function that modifies the behavior of another function or method without changing its source code.

Decorators are a core Python feature and are heavily used in:

Logging

Authentication

Caching

Timing

Access control

Frameworks (Flask, Django)"""

# 1️⃣ Why Do We Need Decorators?
# ❌ Without Decorators (Code Duplication)
def greet():
    print("Before function")
    print("Hello")
    print("After function")

def bye():
    print("Before function")
    print("Goodbye")
    print("After function")
# 🔴 Same logic repeated again & again.
"""
2️⃣ What is a Decorator?

A decorator is a callable that takes another function as input, adds extra functionality, and returns a new function.

In simple words:

Function → Decorator → Enhanced Function"""

# 3️⃣ Functions are First-Class Objects (Foundation)
def hello():
    print("Hello")
x = hello
x()
# Output: Hello


"""✔ Functions can be:

Assigned to variables

Passed as arguments

Returned from functions"""

# 4️⃣ Basic Decorator (Manual Way)
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
def greet():
    print("Hello")

greet = my_decorator(greet)
greet()

"""Output
Before function call
Hello
After function call"""

# 5️⃣ Decorator Using @ Syntax (Pythonic ⭐) important
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()

"""Output   
Before function call
Hello
After function call"""


# ✔ Cleaner
# ✔ Readable
# ✔ Preferred way

# 6️⃣ Decorators with Arguments
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
# Output:
# 5.0
# Cannot divide by zero

# 7️⃣ Generic Decorator Using *args & **kwargs
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
@my_decorator
def add(a, b):
    return a + b
print(add(3, 5))  # 8
# Output:
# Before
# After
# 8 



# ✔ Works for any function

# 8️⃣ Decorators with Return Value
def square_decorator(func):
    def wrapper(n):
        result = func(n)
        return result * result
    return wrapper

@square_decorator
def get_number(n):
    return n

print(get_number(4))  # 16

# 9️⃣ Decorator with Arguments (Advanced)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
say_hi()
# Output:
# Hi
# Hi
# Hi        

# 🔟 Built-in Decorators in Python ⭐
@staticmethod
class Demo:
    @staticmethod
    def show():
        print("Static method")

@classmethod
class Demo:
    @classmethod
    def show(cls):
        print("Class method")

@property
class Demo:
    @property
    def value(self):
        return 10

# 1️⃣1️⃣ Function Caching Decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(50))  # 12586269025
# ✔ Adds caching without changing logic


"""
1️⃣5️⃣ Real-Life Analogy 🧠

Decorator = 🎁 Gift wrapper
Function = 🎁 Gift

Decorator adds:

Logging

Security

Validation
without opening the gift

1️⃣6️⃣ When Should You Use Decorators?

✅ Use when:

Cross-cutting concerns (logging, auth)

Avoiding code duplication

Clean, reusable logic

❌ Avoid when:

Logic is too complex

Debugging becomes unclear

1️⃣7️⃣ Common Mistakes ❌

Forgetting to return wrapper

Not using *args, **kwargs

Ignoring functools.wraps

1️⃣8️⃣ Interview One-Liner

A decorator is a function that modifies another function’s behavior without changing its source code, using function wrapping.

1️⃣9️⃣ Quick Summary
Decorator → function wrapper
@syntax → clean usage
Reusable → powerful → pythonic"""