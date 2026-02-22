#print numbers from 1 to N
def PrintNum(i,N):
    if i==N:
        print(i)
        return
    print(i)
    PrintNum(i+1,N)
N=int(input("enter N value:"))
PrintNum(1,N)

