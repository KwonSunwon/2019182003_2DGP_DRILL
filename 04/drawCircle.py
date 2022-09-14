import turtle

turtle.penup()

i = 0
while i != 6:
    turtle.goto(0 - 100,i * 100 - 100)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    i += 1

turtle.setheading(-90)

i = 0
while i != 6:
    turtle.goto(i * 100- 100, 500- 100)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    i += 1
    
turtle.exitonclick()


