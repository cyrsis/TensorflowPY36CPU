sample = 100


def GlobalMethod():
    global sample
    print("1. Value of sample inside the method is ", str(sample))
    print("2. Change the value to 2")
    sample = 2
    print("3. The new value of 2 is " + str(sample))


if __name__ == '__main__':
    GlobalMethod()
    print("4. The global value of sample outside " + str(sample))
