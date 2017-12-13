import turtle, random

turtle.title('The Turtle Experiment') 
turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(100)
turtle.penup()


def star(sideLength,sideNum):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,sideNum):
        turtle.forward(sideLength)
        turtle.right(720/sideNum)
        turtle.forward(sideLength)
        turtle.left(360/sideNum)
    turtle.penup()
    turtle.end_fill()

for i in range(0,1000):
    starSize = random.randint(3,25)
    x = random.randint(-800,800)
    y = random.randint(-600,600)
    starSides = random.randint(5,9)
    turtle.goto(x,y)
    star(starSize*5/starSides,starSides)
    
