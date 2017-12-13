import math
while True: # forever loop
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break

    print('{} {} {} {}'.format('The square of',num,'is', num**2  ))
    print('{} {}'.format(num**3, 'is the cube'))
    print('{} {}'.format(math.sqrt(num), 'is the square root'))
