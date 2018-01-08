# When to use and when not to use
# Just a way to pass function (expression)



from math import sqrt


def p_pythagorsas(x, y):
    return sqrt(x ** 2 + y ** 2)


print(p_pythagorsas(1, 1))

print((lambda x, y: sqrt(x ** 2 + y ** 2))(1, 1))

l_pythagorsas = lambda x, y: sqrt(x ** 2 + y ** 2)

print(l_pythagorsas(1, 1))


# Reursion requires  a name

def f_factortial(n):
    return 1 if n == 0 else n * f_factortial(n - 1)


print(f_factortial(3))

l_factorial = lambda n: 1 if n == 0 else n * l_factorial(n - 1)

print(l_factorial(3))

# best use case for Lamdba , map, filter
# best use case for Lamdba , map, filter

l = [0, 1, 2, 3, 4]

print(list(map(lambda x: x*2,l)))

