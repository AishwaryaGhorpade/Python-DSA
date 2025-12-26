"""*args collects extra positional arguments into a tuple, and **kwargs collects extra keyword arguments into a dictionary.

| Feature  | `*args`                  | `**kwargs`                     |
| -------- | ------------------------ | ------------------------------ |
| Type     | Tuple                    | Dictionary                     |
| Accepts  | Positional arguments     | Keyword arguments              |
| Use case | Unknown number of values | Unknown number of named values |
| Access   | Index                    | Key                            |


What are *args and **kwargs?

They are used in function definitions to accept a variable number of arguments.

| Syntax     | Stands for                  | Accepts                                  |
| ---------- | --------------------------- | ---------------------------------------- |
| `*args`    | Arbitrary Arguments         | Multiple **positional** arguments        |
| `**kwargs` | Arbitrary Keyword Arguments | Multiple **named (key=value)** arguments |

he names args and kwargs are conventions.
You can use any name, but *args and **kwargs are standard.

"""
# *args – Variable Positional Arguments
# 👉 Problem it solves
# When you don’t know how many values will be passed to a function.

# Example 1: Without *args
def add(a, b):
    return a + b
print(add(3, 5))  # 8
# ❌ Works only for 2 numbers.
# print(add(3, 5, 7))  # Error

# Example 2: With *args
def add(*args):
    print(args)
    return sum(args)

print(add(1, 2, 3, 4))
# Output:
# (1, 2, 3, 4)
# 10
# args is a tuple.

# Example 4: Mixing normal arguments with *args
def greet(name, *messages):
    print("Name:", name)
    for msg in messages:
        print(msg)

greet("Aishwarya", "Good Morning", "Welcome", "Have a nice day")
# Output:
# Name: Aishwarya
# Good Morning
# Welcome
# Have a nice day

# Rule: Normal parameters must come before *args.

# **kwargs – Variable Keyword Arguments
# 👉 Problem it solves

# When you don’t know how many named arguments will be passed.

# Example 1: Basic **kwargs
def show_details(**kwargs):
    print(kwargs)

show_details(name="Aishwarya", age=24, city="Pune")

# Output:
# {'name': 'Aishwarya', 'age': 24, 'city': 'Pune'}


# 📌 kwargs is a dictionary

# Example 3: Mandatory arguments + **kwargs
def employee(id, **details):
    print("ID:", id)
    print(details)

employee(101, name="Riya", salary=50000)

# Output:
# ID: 101
# {'name': 'Riya', 'salary': 50000} 


# 📌 Rule: Normal parameters must come before **kwargs.

"""Using *args and `**kwargs Together
Order is IMPORTANT:
def func(a, b, *args, **kwargs):
    pass

Correct Order:

Normal arguments

*args

**kwargs"""

def demo(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, 4, x=10, y=20)
# Output:
# a: 1
# b: 2      
# args: (3, 4)
# kwargs: {'x': 10, 'y': 20}

# Unpacking with * and **
# Unpacking List/Tuple using *
nums = [1, 2, 3]
print(*nums)
# Output:
# 1 2 3

# Unpacking Dictionary using **
def greet(name, age):
    print(name, age)

data = {"name": "Aishwarya", "age": 24}
greet(**data)
# Output:
# Aishwarya 24  