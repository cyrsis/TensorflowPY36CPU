#setup
import turtle
turtle.shape('turtle')
turtle.colormode(255)
turtle.pensize(1)
turtle.pencolor(0,255,0)
turtle.fillcolor(0,0,0)
turtle.speed(200)
turtle.bgcolor(0,0,0)

def spiral(angle,distance):
    if distance < 2:
        print('done')
    if angle >100:
        print('done')
    else:
        turtle.forward(distance)
        turtle.left(angle)
        spiral(angle**1.02,distance)

turtle.left(40)
spiral(2,5)
turtle.ht()



