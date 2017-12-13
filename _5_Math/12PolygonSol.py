import turtle

turtle.title('The Turtle Experiment') 
turtle.shape('turtle')
turtle.color('yellow')
turtle.fillcolor('white')
turtle.bgcolor('black')
turtle.pensize(2) 

def polygon(sideLength,sideNum):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,sideNum):
        turtle.forward(sideLength)
        turtle.left(360/sideNum)
    turtle.penup()
    turtle.end_fill()
    turtle.hideturtle()
   


