def sweet(x):
    return (x + abs(x)) ** 3


def filterPositive(x):
    return x > 0


print(list(map(sweet, range(-4, 5))))

print(list(filter(filterPositive, (map(sweet, range(-4, 5 ))))))


# print(list(filter(filterPositive(range(-4,5)))))

def Negative(x):
    return x > 0


print(list(filter(Negative, (map(sweet, range(2, 200))))))
