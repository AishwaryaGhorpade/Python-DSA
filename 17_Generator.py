"""A generator in Python is a special type of function that returns values one at a time, on demand, instead of returning all values at once.making programs memory-efficient and faster for large data sets.

Generators are used for:

Memory-efficient iteration

Handling large data

Streaming data processing"""

# Why Do We Need Generators?
# ❌ Problem with normal functions
"""
def square_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result
print(square_list(1000000))"""
# 🔴 Problem:
# Stores all values in memory

# Slower for large data

"""What is a Generator?

A generator:

Uses yield instead of return

Returns an iterator object

Pauses execution after yield

Resumes from same point next time"""

# 3️⃣ Simple Generator Example
def squares(n):
    for i in range(n):
        yield i * i
gen = squares(5)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

#using for loop 
for value in squares(5):
    print(value)
# Output:
# 0         
# 1
# 4
# 9
# 16    

# No next() required
# ✔ Automatically handles StopIteration


# Generator Execution Flow (Important)
def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = demo()
next(g)   # Start → 1
next(g)   # Middle → 2
next(g)   # End → StopIteration

#ouput:
# Start
# Middle
# End   

"""| Feature        | yield               | return             |
| -------------- | ------------------- | ------------------ |
| Returns        | One value at a time | All values at once |
| Function state | Paused & resumed    | Ends               |
| Memory usage   | Low                 | High               |
| Stop           | StopIteration       | Function exit      |"""

# Generator Expression (Short Syntax ⭐)important

# Like list comprehension but uses ()

gen = (i * i for i in range(5))

print(next(gen))  # 0
print(next(gen))  # 1

# Compare
list_comp = [i*i for i in range(5)]  # list
gen_exp  = (i*i for i in range(5))   # generator

# 8️⃣ Memory Comparison (Very Important)
import sys

list_comp = [i*i for i in range(100000)]
gen_exp = (i*i for i in range(100000))

print(sys.getsizeof(list_comp))  # very large
print(sys.getsizeof(gen_exp))    # very small
# Output:   
# 876112
# 112

# 9️⃣ Infinite Generator
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1
gen = infinite_numbers()
for _ in range(5):
    print(next(gen))
# Output:
# 1
# 2
# 3     
# 4
# 5 

"""| Feature            | Generator | Iterator               |
| ------------------ | --------- | ---------------------- |
| Created using      | `yield`   | `__iter__`, `__next__` |
| Code size          | Small     | More boilerplate       |
| Auto StopIteration | Yes       | Manual                 |
| Memory Efficient   | Yes       | Yes                    |"""

# Real-World Example: Reading Large File 📁
def read_large_file(file):
    with open(file) as f:
        for line in f:
            yield line


# ✔ Reads one line at a time
# ✔ Saves memory

# 1️⃣2️⃣ Using Generator with send() (Advanced)
def counter():
    num = 0
    while True:
        received = yield num
        if received == "reset":
            num = 0
        else:
            num += 1

c = counter()
next(c)
c.send("reset")
print(c.send(None))  # 1
print(c.send(None))  # 2
# Output:   
# 1
# 2

# 1️⃣3️⃣ yield from (Python 3.3+)
def sub_gen():
    yield 1
    yield 2

def main_gen():
    yield from sub_gen()
    yield 3
for value in main_gen():
    print(value)

# Output:

# 1 2 3

"""1️⃣4️⃣ When Should You Use Generators?

✅ Use when:

Large datasets

Streaming data

Infinite sequences

Performance optimization

❌ Avoid when:

Random access needed

Small datasets

1️⃣5️⃣ Common Mistakes ❌

Trying to reuse exhausted generator

Forgetting StopIteration

Using return instead of yield

1️⃣6️⃣ Interview One-Liner

A generator is a function that produces values lazily using yield, making programs memory-efficient and faster for large data sets.

1️⃣7️⃣ Quick Summary
yield → pause function
next() → resume function
generator → iterator"""
