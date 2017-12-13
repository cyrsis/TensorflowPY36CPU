import turtle, random, time

turtle.title('The Turtle Experiment') 
turtle.shape('turtle')
turtle.color('white')
turtle.fillcolor('white')
turtle.bgcolor('skyblue')
turtle.pensize(2)
turtle.speed(100)
turtle.penup()
cloudDone = False


def semiCircle(size):
    turtle.pendown()
    for i in range(0,20):
        turtle.forward(size)
        turtle.left(9)
    turtle.left(180)

def adjustTurn():
    heading = turtle.heading()
    randTurn = random.randint(1,10)
    if heading >= 50 and heading<=140:
        turtle.left(randTurn*2)
    if heading > 140 and heading<=220:
        turtle.left(randTurn*10)
    if heading > 220 and heading<=270:
        turtle.left(randTurn*2)
    if heading > 270 and heading<50:
        turtle.left(randTurn)

def homeCheck():
    global cloudDone
    if turtle.xcor() > 0:
        distance = turtle.distance(0,0)
        turtle.setheading(0)
        turtle.left(turtle.towards(0,0))
        turtle.forward(distance/2)
        turtle.dot(distance)
        turtle.end_fill()
        cloudDone = True

def cloud():
    turtle.left(50)
    global cloudDone
    cloudDone = False 
    turtle.begin_fill()
    for i in range(0,5):
        size = random.randint(3,7)
        semiCircle(size)
        adjustTurn()
    while cloudDone == False:
        size = random.randint(3,7)
        semiCircle(size)
        adjustTurn()
        homeCheck()
    turtle.end_fill()

cloud()


#Draw a semi circle


#Adjust a turn


#Go back to orign


