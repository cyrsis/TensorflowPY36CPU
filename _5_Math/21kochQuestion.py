#setup
import turtle
turtle.shape('turtle')
turtle.colormode(255)
turtle.pensize(1)
turtle.pencolor(0,255,0)
turtle.fillcolor(0,0,0)
turtle.speed(50)
turtle.bgcolor(0,0,0)


def kochSection(size):
    turtle.forward(size/3)
    turtle.left(60)
    turtle.forward(size/3)
    turtle.right(120)
    turtle.forward(size/3)
    turtle.left(60)
    turtle.forward(size/3)
   

def kochSuperSection(size):
    kochSection(size/3)
    turtle.left(60)
    kochSection(size/3)
    turtle.right(120)
    kochSection(size/3)
    turtle.left(60)
    kochSection(size/3)

def kochSuperDuperSection(size):
    kochSuperSection(size/3)
    turtle.left(60)
    kochSuperSection(size/3)
    turtle.right(120)
    kochSuperSection(size/3)
    turtle.left(60)
    kochSuperSection(size/3)
    


kochSuperDuperSection(300)


turtle.ht()



