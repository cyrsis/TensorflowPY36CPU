#setup
import turtle, random
turtle.shape('turtle')
turtle.colormode(255)
turtle.pensize(1)
turtle.pencolor(0,255,0)
turtle.speed(1000)
turtle.bgcolor(0,0,0)


def kochSection(size,order):
    if order == 0:
        turtle.forward(size)
    else:
        kochSection(size/3,order-1)
        turtle.left(60)
        kochSection(size/3,order-1)
        turtle.right(120)
        kochSection(size/3,order-1)
        turtle.left(60)
        kochSection(size/3,order-1)
   


kochSection(300,4)

turtle.ht()



