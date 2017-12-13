
import turtle, random, time


#Select a color scheme
turtle.shape('turtle')
turtle.color('white')
turtle.bgcolor('sky blue')
turtle.fillcolor('white')
turtle.speed(100)
cloudDone = False
x = -200
y = 0




def semiCircle(size):
    for i in range(0,20):
        turtle.forward(size)
        turtle.left(9)
    turtle.right(180)


def adjustTurn():
    randTurn = random.randint(1,10)
    heading = turtle.heading()
    if heading >=50 and heading <=140:
        turtle.left(randTurn*2)
    elif heading >140 and heading <=220:
        turtle.left(randTurn*10)
    elif heading >220 and heading <=270:
        turtle.left(randTurn*2)
    elif heading > 270 and heading <50:
        turtle.left(0)


def homeCheck():
    global x
    global cloudDone
    if turtle.xcor() > x:
        turtle.setheading(0)
        turtle.left(turtle.towards(x,0))
        distance = turtle.distance(x,0)
        turtle.forward(distance/2)
        turtle.dot(distance)
        turtle.end_fill()
        cloudDone = True


def drawCloud():
    global cloudDone
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    cloudDone = False
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.left(50)
    
    for i in range(0,10):
        size = random.randint(1,4)
        semiCircle(size)
        adjustTurn()
        
    while cloudDone == False:
        size = random.randint(2,5)
        semiCircle(size)
        adjustTurn()
        homeCheck()
    turtle.penup()

drawCloud()
x = 200
drawCloud()



    

#Draw a circle

turtle.hideturtle()


#Draw a half circle

#Draw a series of half circles

#Bend them inwards

#Figure out how to tie up the last gap
