import turtle

turtle.title('The Turtle Experiment') 
turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize(5) 

def circle():
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,72):
        turtle.forward(10)
        turtle.left(5)
    turtle.penup()
    turtle.end_fill()
    

def square():
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(200)
        turtle.left(90)
    turtle.penup()
    turtle.end_fill()
    

def triangle():
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,3):
        turtle.forward(200)
        turtle.left(120)
    turtle.penup()
    turtle.end_fill()

    

circle()
turtle.goto(-450,0)
triangle()
turtle.goto(300,0)
square()

