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
   
def kochSnowflake(size,order):
    kochSection(size,order)
    turtle.right(120)
    kochSection(size,order)
    turtle.right(120)
    kochSection(size,order)


for i in range(0,100):
    turtle.penup()
    x = random.randint(-700,700)
    y = random.randint(-400,400)
    turtle.goto(x,y)
    size = random.randint(30,200)
    order = random.randint(0,4)
    turtle.pendown()
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    kochSnowflake(size,order)
    turtle.end_fill()
    



kochSnowflake(300,2)

turtle.ht()



