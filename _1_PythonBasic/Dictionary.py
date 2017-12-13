# Dictionary iterm are in brackets {} in key: values pairs

print("Data")
cars = {'factory': 'bmw',
        'model': '550i',
        'year': '2016'}

print(cars)

print("#" * 40)
print("Access by keys")
print(cars['model'])

print("#" * 40)

print("Nested Dictionary")

nestedcars = {'bmw': {'factory': 'bmw', 'model': '550i', 'year': '2016'},
              'benz': {'factory': 'benz', 'model': 'benz 50i', 'year': '2017'}}

print(nestedcars['bmw']['year'])

print("#" * 40)
print("The keys in the nested Cars")
print(nestedcars.keys())

print("The values in the nested cars")
print(nestedcars.values())

print("The items in dict")
print(nestedcars.items())

print("#" * 40)

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3, 'B': 10}

mcase_frequency = {
    k.lower():
        mcase.get(k.lower(), 0) +
        mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

frquence = {
    b.lower():  # this is a function
        mcase.get(b.upper(), 0) +
        mcase.get(b.lower(), 0)
    for b in mcase.keys()

}

print(frquence)

print(mcase_frequency)
# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}

print({v: k for k, v in mcase.items()})

print("Here is the line "+ str([x ** 2 for x in range(10)]))
