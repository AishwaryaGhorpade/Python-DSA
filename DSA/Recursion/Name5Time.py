#Print name 5 times using recursion
def printName(i,name):
    if i==5:
        return
    print(i+1,name)
    i+=1
    printName(i,name)
name=input("enter name:")
printName(0,name)
