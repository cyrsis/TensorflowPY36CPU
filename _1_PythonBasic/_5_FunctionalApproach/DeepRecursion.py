def p_factorial(n):
    f = 1
    for i in range(1, n + 1):#including 1
        f *= i
    return f


print(p_factorial(0))
print(p_factorial(2))
print(p_factorial(4))


def f_factorial(n):
    return 1 if n ==0 else n*f_factorial(n-1)

print(f_factorial(0))
print(f_factorial(2))
print(f_factorial(4))
