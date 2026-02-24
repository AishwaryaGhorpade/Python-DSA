def FibbanacciNum(n):
    if n<=1:
        return n
    return FibbanacciNum(n-1)+FibbanacciNum(n-2)
n=int(input("Enter n:"))
print(FibbanacciNum(n))