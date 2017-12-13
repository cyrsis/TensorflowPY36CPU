def factorial(n):
    f = 1
    for i in range(1,n+1):
        f=f*i
    return f

def factorialRecursive(n):
    if n<1:
        return 1
    else:
        return n * factorialRecursive(n-1)
        
