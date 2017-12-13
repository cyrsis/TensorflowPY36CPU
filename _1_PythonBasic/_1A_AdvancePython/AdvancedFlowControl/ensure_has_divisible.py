

def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor

items = [2, 25, 9, 37, 24, 28, 14, 21]
divisor = 7

dividend = ensure_has_divisible(items, divisor)

print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))

# --------------For Else is so bad then we have do some refractor-------
for item in items:
    if item % divisor == 0:
        found = item
        break
else:  # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))


# Maybe using Yield is much better?
