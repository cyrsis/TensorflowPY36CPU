#And OR can make a flow control

# ========================================================================= #
#                              "AND"    and "OR"                                   #
# Give the first value tghat insnt True,
#  The result ios not evaluated
#  may result hard to read                                                   #
# ========================================================================= #


def my_and(*values):
    for value in values:
        if not value:
            return value

    return value


def my_or(*values):
    for value in values:
        if value:
            return value
    return value


print(my_and('a','b','c') == ('a' and 'b' and 'c'))
print(my_or('a','b','c') == ('a' or 'b' or 'c'))

ANIMALS = 'mammal','reptile','amphibian', 'bird'
EGG_LAYING_ANIMALS ='reptile','amphibian','bird'

is_animal = lambda animal: animal in ANIMALS
animal_lays_eggs = lambda animal:print('animal lays eggs call') or animal in EGG_LAYING_ANIMALS

lays_eggs = lambda thing : is_animal(thing) and animal_lays_eggs(thing)
print(lays_eggs('reptile'))