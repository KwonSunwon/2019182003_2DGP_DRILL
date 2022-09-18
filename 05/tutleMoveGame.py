import turtle

def moveLeft():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def moveRight():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def moveUp():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def moveDown():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(moveLeft, 'a')
turtle.onkey(moveRight, 'd')
turtle.onkey(moveUp, 'w')
turtle.onkey(moveDown, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()

turtle.exitonclick()
