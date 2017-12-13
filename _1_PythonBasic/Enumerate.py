#Enum can do sort of print different way

my_list = ['apple', 'organge', 'candy']

for key, value in enumerate(my_list,2):
    print(key, value)

print("#" * 40)

for key, value in enumerate(my_list, 5):
    print(key, value)



# 2 apple
# 3 organge
# 4 candy


print("#" * 40)

print(list(enumerate(my_list, 2)))
# [(2, 'apple'), (3, 'organge'), (4, 'candy')]
