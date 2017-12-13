from random import choice


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Hello {name}'.format(name=self.name)
    
    def yellMyName(self):
        print("I am a person and my name is " + self.name)


def main():
    people = [
        Person('Jane'),
        Person('Jill'),
        Person('Victor')
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()

print("#" * 40)
sampleStrig = "This is a text"

sampleStrig.upper()

print("Type of the object in here " + str(type("st")) + "In the string 'St'")

print("#" * 40)
print("Inheritance from the Upper Class")


class CrazyPerson(Person):
    def __init__(self, Name):
        self.Name = Name

    def yellMyName(self): #override method in python
        super(CrazyPerson,self).yellMyName()
        print("I am Crazy person with Name " + self.Name)
        


victor = CrazyPerson('Victor')

print(victor.Name)
print(victor.yellMyName())
