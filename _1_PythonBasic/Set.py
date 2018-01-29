squared = {x**2 for x in [1, 1, 2]}

print(squared)
# Output: {1, 4}

print({x ** 2 for x in [5, 2, 6]})

my_set = set(['one','two','three'])
my_set2 = set(['one','two','three','four'])
print(set.union(my_set,my_set2))
print(set.intersection(my_set,my_set2))
print(set.difference(my_set2,my_set))
