"""What is Operator Overloading?

Operator Overloading means using operators like:

+

-

*

==

<

>

etc.

with user-defined objects, allowing them to behave in your custom way.

For example:

3 + 5      # numeric addition
"A" + "B"  # string concatenation
[1] + [2]  # list merging


The same operator behaves differently → polymorphism.

Python allows you to define this behavior for your own classes using special methods (dunder methods).

🔹 Why Operator Overloading?

Because normal operators don’t work on objects:

class Book:
    def __init__(self, pages):
        self.pages = pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)      # ❌ ERROR


Python doesn’t know how to add two Book objects.

So we overload the operator to define behavior.

🔥 How Operator Overloading Works?

Each operator has a corresponding magic method.

Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
%	__mod__(self, other)
==	__eq__(self, other)
<	__lt__(self, other)
>	__gt__(self, other)
str(obj)	__str__()

Let’s implement each one with examples."""

# ⭐ 1. Overloading + Operator
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)       # Output: 300
# Now + works on Book objects!


# ⭐ 2. Overloading > Operator
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages

b1 = Book(150)
b2 = Book(120)

print(b1 > b2)      # True

# ⭐ 3. Overloading == Operator
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __eq__(self, other):
        return self.pages == other.pages
b1 = Book(100)      
b2 = Book(100)
b3 = Book(150)      
print(b1 == b2)     # True
print(b1 == b3)     # False 

# ⭐ 4. Overloading * Operator

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __mul__(self, other):
        return self.pages * other.pages

b1 = Book(10)
b2 = Book(20)
print(b1 * b2)     # Output: 200

# ⭐ 5. Overloading str() Function

# print(obj) internally calls __str__().

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with {self.pages} pages"

b = Book(150)
print(b)     # Book with 150 pages

# 🔹 Operator Overloading with Different Types

# You can also do:
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        if isinstance(other, int):
            return self.pages + other
        elif isinstance(other, Book):
            return self.pages + other.pages
b = Book(100)
print(b + 50)        # 150
b2 = Book(200)
print(b + b2)       # 300


# 🔹 Another Real-Life Example: Vector Addition
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f"({self.a}, {self.b})"

v1 = Vector(2, 3)
v2 = Vector(1, 5)

print(v1 + v2)     # (3, 8)

"""🔹 Important Points (Interview Notes)
✔ Operator Overloading uses magic methods
✔ Allows custom operations on objects
✔ Improves readability
✔ Enables polymorphism
✔ Should be used carefully (avoid confusing behavior)
🔹 Common Magic Methods for Operators
Purpose	Method
Addition	__add__
Subtraction	__sub__
Multiplication	__mul__
Power	__pow__
True Division	__truediv__
Floor Division	__floordiv__
Modulus	__mod__
Unary minus	__neg__
Less than	__lt__
Greater than	__gt__
Equals	__eq__
Not equals	__ne__
String representation	__str__
⭐ Final Summary

Operator overloading allows:

✔ Using operators (+ - * > ==) with objects
✔ Defining custom behavior using magic/dunder methods
✔ More readable and natural code
✔ A form of compile-time polymorphism in Python

Examples:

Use __add__ to overload +

Use __gt__ to overload >

Use __str__ to define object printing"""