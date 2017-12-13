
for i in range(0,13):
    s = '*'+i*'**' 
    print(s.center(25,' '))

def pyramid(height):
    width = height * 2
    for i in range(0,height):
        s = '*'+i*'**' 
        print(s.center(width,' '))
