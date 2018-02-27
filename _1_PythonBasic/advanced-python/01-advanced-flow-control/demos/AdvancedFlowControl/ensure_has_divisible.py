

def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor

items = [2, 25, 9, 37, 24, 28, 14]
divisor = 12

dividend = ensure_has_divisible(items, divisor)

print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))



