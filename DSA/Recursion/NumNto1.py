#print numbers from N to 1
def PrintNum(N):
    if N==1:
        print(N)
        return
    print(N)
    PrintNum(N-1)
N=int(input("enter N value:"))
PrintNum(N)