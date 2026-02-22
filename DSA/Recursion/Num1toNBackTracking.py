def printNum(N):
    if N==1:
        print(N)
        return
    printNum(N-1)
    print(N)
    return
N=int(input("Enter N:"))
printNum(N)