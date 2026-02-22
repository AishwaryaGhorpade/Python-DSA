#1st way

# def SumOfN(N,sum):
#     if N<1:
#         print("sum:",sum)
#         return
#     SumOfN(N-1,sum+N)

#2nd way
def SumOfN(N):
    if N==0:
        return 0
    return N+SumOfN(N-1)

N=int(input("Enter N:"))
# print(SumOfN(N,0))  #1st method calling
print(SumOfN(N))
