def sum_sum(x=2, y=4):
    return x+y


print(sum_sum(1,2))

print("#" * 40)
print("Function return True or False")

def isCity(city):
    citys = ['Hong Kong', 'China', 'Canada']
    if city in citys:
        return True

    else:
        return False



print(isCity('State'))

print("#" * 40)
print("Function can do concat too")
print(sum_sum("one","two"))

print("#" * 40)
print("Default pararmenters")
print(sum_sum())


