num=int(input("Enter number between 5-9: "))
if num<5 or num>9:
    raise ValueError("value is not between 5-9")
print("End!!")

# output
# Enter number between 5-9: 1
# Traceback (most recent call last):
#   File "/Users/aishwaryaghorpade/Desktop/DSA/Raise.py", line 3, in <module>
#     raise ValueError("value is not between 5-9")
# ValueError: value is not between 5-9

# Enter number between 5-9: 6
# End!!