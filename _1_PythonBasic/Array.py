#mMaybe this is call a list, I wasnt really sure

cars = ["bmw","honda","audi"]



print("The length of array " + str(len(cars)))

cars.insert(1,"jeep")

print(cars)

print("The index of jeep is " + str(cars.index("jeep")))

print("#" * 40)

print("Array Slice")
print(cars[0:2])

print("#" * 40)

print('Array Sorting')
print("Before sorting")
print(cars)
print("Afte sorting")
print(cars.sort())
print(cars)

