#tuples are like list but
#they are immutavle

print("List of Numbers")
print("#" * 40)
listOfNumbers = [1,2,3]

print(listOfNumbers)


print("#" * 40)
print("Orgini al Tuples")
tupleOfNumnbers = (1,2,3)
print(tupleOfNumnbers)

print("Tuples access by index")
print(tupleOfNumnbers[0])

print("Tuples skip 1 by [:1]")
print(tupleOfNumnbers[1:])

print("Count how many match in tupl")
print(tupleOfNumnbers.count(3))

print("Ask where is the index of the values is ")
print(tupleOfNumnbers.index(2))
