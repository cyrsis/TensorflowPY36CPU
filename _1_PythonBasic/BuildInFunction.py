""""


"""


def Largest_num(*args):
    print(max(args))


def Smallest_num(*args):
    print("The list is "+str(args))
    print("The smallest number from the list "+str(min(args)))


def main():
    Largest_num(-20,-10,0,10,100 )
    Smallest_num(-10,0,20)
    print("Build in function call abs() " + str(abs(10)))

if __name__ == '__main__':
    main()