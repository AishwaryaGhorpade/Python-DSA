"""Regex is a powerful text processing tool used for pattern matching, extraction, and validation.
A Regular Expression is a pattern used to:

Search text

Match text

Extract data

Validate input

Replace text

📌 Python provides the re module for regex operations.

2️⃣ Importing the Regex Module
import re

| Function        | Purpose                      |
| --------------- | ---------------------------- |
| `re.match()`    | Match at **start** of string |
| `re.search()`   | Match **anywhere** in string |
| `re.findall()`  | Return **all matches**       |
| `re.finditer()` | Return iterator of matches   |
| `re.sub()`      | Replace matches              |
| `re.split()`    | Split string using regex     |
"""
# re.match() – Match at Start Only
import re

text = "Python is powerful"
result = re.match("Python", text)

print(result)

# Output:
# <re.Match object; span=(0, 6), match='Python'>

# ✔ Matches because string starts with Python
#returns None if no match found
# ❌ Fails if pattern is not at start.

# re.search() – Search Anywhere
# ✔ Finds match anywhere in string
text = "I love Python"
result = re.search("Python", text)

print(result.group())

# Output:
# Python


# re.findall() – Find All Matches
text = "cat bat rat mat"
result = re.findall("at", text)

print(result)

# Output:
# ['at', 'at', 'at', 'at']

# re.finditer() – Match with Positions
text = "apple apple apple"
matches = re.finditer("apple", text)

for m in matches:
    print(m.start(), m.end(), m.group())

# Output:
# 0 5 apple
# 6 11 apple
# 12 17 apple

"""Regex Special Characters (Metacharacters)
Character Matching
| Pattern | Meaning                      |    |
| ------- | ---------------------------- | -- |
| `.`     | Any character except newline |    |
| `^`     | Start of string              |    |
| `$`     | End of string                |    |
| `*`     | 0 or more                    |    |
| `+`     | 1 or more                    |    |
| `?`     | 0 or 1                       |    |
| `{n}`   | Exactly n times              |    |
| `{n,m}` | Between n and m              |    |
| `       | `                            | OR |
| `()`    | Grouping                     |    |

Character Classes
| Pattern  | Meaning           |
| -------- | ----------------- |
| `[abc]`  | a or b or c       |
| `[a-z]`  | lowercase letters |
| `[A-Z]`  | uppercase letters |
| `[0-9]`  | digits            |
| `[^0-9]` | Not digits        |

Predefined Character Sets
| Pattern | Meaning            |
| ------- | ------------------ |
| `\d`    | Digit (0–9)        |
| `\D`    | Non-digit          |
| `\w`    | Alphanumeric + `_` |
| `\W`    | Non-word           |
| `\s`    | Whitespace         |
| `\S`    | Non-whitespace     |

"""

text = "abc123XYZ"
print(re.findall("[a-z]", text))
# Output:
# ['a', 'b', 'c']

re.findall("ab*", "ab abb abbb a")
# Output:
# ['ab', 'abb', 'abbb', 'a'] 

text = "My number is 9876543210"
match = re.search(r"(\d{10})", text)

print(match.group())
# Output:
# 9876543210    
# r before string makes it raw string
# Important for \d, \w, etc.

text = "Date: 25-12-2025"
match = re.search(r"(\d{2})-(\d{2})-(\d{4})", text)

print(match.groups())
# Output:
# ('25', '12', '2025')  

# Non-Capturing Groups
re.findall("(?:ab)+", "ababab")
# Output:
# ['ababab']    


# 1️⃣4️⃣ Anchors
# Pattern	Meaning
# ^hello	Starts with hello
# world$	Ends with world
# 1️⃣5️⃣ Lookahead & Lookbehind (Advanced)
# Positive Lookahead

re.findall(r"\d+(?=kg)", "10kg 20kg 30")
# Output:
# ['10', '20']

# Negative Lookahead
re.findall(r"\d+(?!kg)", "10kg 20 30kg")
# Output:
# ['20']

# 1️⃣6️⃣ re.sub() – Replace Text
text = "I love Java"
new_text = re.sub("Java", "Python", text)
print(new_text)
# Output:
# I love Python


# 1️⃣7️⃣ re.split() – Split Using Regex
print(re.split(r"[,;\s]", "apple,banana;grape mango"))
# Output:
# ['apple', 'banana', 'grape', 'mango']

# 1️⃣8️⃣ Raw Strings (r"") – VERY IMPORTANT
print(re.findall(r"\d+", "123 abc"))
# Output:
# ['123']


""" Avoids escaping backslashes

1️⃣9️⃣ Regex Flags
Flag	Meaning
re.I	Ignore case
re.M	Multiline
re.S	Dot matches newline
re.findall("python", text, re.I)"""

# 2️⃣0️⃣ Real-World Use Cases

# ✔ Email Validation
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# ✔ Phone Number Validation
r"^[6-9]\d{9}$"

# ✔ Password Validation
r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

"""2️⃣1️⃣ 
Common Regex Mistakes ❌

Forgetting r""

Overusing .*

Missing anchors ^ and $

Confusing match() with search()

2️⃣2️⃣ Regex Summary
Concept	Use
Match	match()
Search	search()
Extract	findall()
Replace	sub()
Validate	Anchors + Pattern"""
