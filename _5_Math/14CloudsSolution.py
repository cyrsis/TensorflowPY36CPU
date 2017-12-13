import turtle, random, time

turtle.title('The Turtle Experiment') 
turtle.shape('turtle')
turtle.color('white')
turtle.fillcolor('white')
turtle.bgcolor('skyblue')
turtle.pensize(2)
turtle.speed(100)
turtle.penup()

def cloud(cloudX,cloudY):
    turtle.goto(cloudX,cloudY)
    for i in range(0,45):
        x = random.randint(cloudX-100,cloudX+100)
        y = random.randint(cloudY-30,cloudY+30)
        size = random.randint(20,90)
        turtle.goto(x,y)
        turtle.dot(size)

def populateClouds(number):
    for i in range(0,number):
        x = random.randint(-700,700)
        y = random.randint(-200,600)
        cloud(x,y)

populateClouds(20)
