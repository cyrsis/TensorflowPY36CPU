import timeit

print(timeit.timeit('x=2+2'))
print(timeit.timeit('x=sum(range(10))'))
