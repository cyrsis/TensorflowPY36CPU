# anything iterable is
# __iter__
# __getitem__

var = "Some string"
listOfNumber = [2, 4, 5, 6, 7]

# Why we need iterator, because we need to save memory


my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) #For loop would stop the errors


def genenerateFunction():
    for i in range(10):
        yield i
# yield is fancy for pop put 1 item at the time.
# kind of important for async world

for variable1 in genenerateFunction():
    print(variable1)
