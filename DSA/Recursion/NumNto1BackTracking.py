def printNum(i,N):
    if i==N:
        print(i)
        return
    printNum(i+1,N)
    print(i)
    return
N=int(input("Enter N:"))
printNum(1,N)