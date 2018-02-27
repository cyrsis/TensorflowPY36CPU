


items = [2, 25, 9, 37, 24, 28, 14]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:  # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))



