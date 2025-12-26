def Fibonacci(n):
    if n==0 or n==1:
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)
num=int(input("Enter a number: "))
print(Fibonacci(num))

# TC=O(2^n) and SC=O(2^n). every eteration calls 2 fib function so 2^n.

# output
# Enter a number: 7
# 13