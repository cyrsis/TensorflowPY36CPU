print("For Loop ing string")
name = "Victor"
for c in name:
    print(c, end='')
print()
print("#" * 40)
print("For loop in collections ")
cars = ["BMW", "Toyota", "Honda"]
for car in cars:
    print(car)

print("#" * 40)
print("For loop in Dic")

words = {'one': 1, 'two': 2}
words2 = dict(one=1, two=2)

for word in words2:
    print(word + " " + str(words2[word]))

print("#" * 40)

print("Access key and value at the same time")
for k, v in words2.items():
    print(k)
    print(v)

print("#" * 40)

# variable = [out_exp for out_exp in input_list if out_exp == 2]
list = [i for i in range(200)]

print(list)
getListOfInt = [i for i in range(200) if i != 10]
square = [i ** 2 for i in range(10)]
print(square)
