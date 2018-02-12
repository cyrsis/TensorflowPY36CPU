import turtle, random

turtle.title('The Turtle Experiment')
turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(1)
turtle.penup()


def star(sideLength, sideNum):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0, sideNum):
        turtle.forward(sideLength)
        turtle.left(720 / sideNum)
        turtle.forward(sideLength)
        turtle.right(360 / sideNum)
    turtle.penup()
    turtle.end_fill()


star(200, 8)
