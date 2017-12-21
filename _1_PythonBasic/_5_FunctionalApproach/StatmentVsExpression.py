#Statment is
#if ,if for, def, class
# do not evlaute to something
#can not print the result


# ========================================================================= #
#                              Statement in general                         #
# :                                                                         #
# ========================================================================= #

#assignment
x = 0
x +=1 #expression do not use assignment


#branch
if x ==1:
    print('X==1')
elif x == 2:
    print('X==2')
else:
    print("X not in [1,2]")

#loop ,

for x in range(2):
    print(x**2)

while True:
    break

#Function, Generator and Class definitions
#All statments

class MyClass:
    pass

def my_function(x):
    return x*2

def my_generator(x):
    yield x*2

#import OS
#assert True
#pass
#del x
try:
    raise Exception()
except:
    pass

# with open('./') as fd:
    pass

# ========================================================================= #
#                              Expression in Pure form                      #
# :                                                     #
# ========================================================================= #

#Expressions
#alwasys return something that can print out

#value are expressions
print(10*2)
print(print(10))#Functions call are expression 
print([x*2 for x in range(2)]) #List are expression


