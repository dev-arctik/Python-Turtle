
import turtle
pen = turtle.Turtle()

pen.color("red")
pen.speed(0)
pen.hideturtle()

for i in range(0,21):
    x = 0
    y = (10-(0.5*i)) * 25
    x1 = 0.5*i * 25
    y1 = 0
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.goto(x1,y1)

for i in range(0,21):
    x = 0
    y = (10-(0.5*i)) * 25
    x1 = 0.5*i * 25
    y1 = 0
    pen.penup()
    pen.goto(x1,-y1)
    pen.pendown()
    pen.goto(x,-y)
    

for i in range(0,21):
    y = 0
    x = -(10-(0.5*i)) * 25
    y1 = -0.5*i * 25
    x1 = 0
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.goto(x1,y1)


for i in range(0,21):
    x = 0
    y = (10-(0.5*i)) * 25
    x1 = 0.5*i * 25
    y1 = 0
    pen.penup()
    pen.goto(-x,y)
    pen.pendown()
    pen.goto(-x1,y1)
