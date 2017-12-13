# import the math lib, this is for math.sqrt() function
import math

print('enter your number:')
#convert user input to an integer 
userNum = int(input())
# store the square of userNum in the variable square
square = userNum**2
# store the cube of userNum in the variable cube
cube = userNum**3
# store the square root of userNum in the variable root
root = math.sqrt(userNum)

# notice how varible userNum, square, cube, root
# ALL need to be converted to a string in the print statement
print('the square of '+ str(userNum) + ' is ' + str(square))
print('the cube of '+ str(userNum) + ' is ' + str(cube))
print('the square root of '+ str(userNum) + ' is ' + str(root))

