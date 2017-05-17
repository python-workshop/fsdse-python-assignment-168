"""def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) """
def fib_recursive(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib_recursive(n-1) + fib_recursive(n-2)
print(fib_recursive(9)) 

# Dynamic 

cache = {}
def fib_dynamic(n):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2,)
        return cache[n]
print(fib_dynamic(9))


 # iterative
def fib_iterative(n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
print(fib_iterative(9))



