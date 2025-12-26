class ageTooSmallError(Exception):
    pass
def registerToFunction(age):
    if age < 18:
        raise ageTooSmallError("Age must be 18 or above to register!!")
    return "sucessufully registered!!"
try:
    age=int(input("Enter age: "))
    print(registerToFunction(age))
except ageTooSmallError as e:
    print(e)


# output
# Enter age: 12
# Age must be 18 or above to register!!

# Enter age: 55
# sucessufully registered!!