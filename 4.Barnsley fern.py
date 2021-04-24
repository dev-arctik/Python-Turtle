import turtle
import random
pen = turtle.Turtle()

pen.speed(0)
pen.color('green')
pen.penup()
pen.hideturtle()

x = 0
y = 0
for n in range(100000):
    r = random.random()
    r = r*100
    print('r:{}\nx:{}  y:{}'.format(r,x,y))
    pen.goto(85*x,57*y-275)
    pen.pendown()
    pen.dot()
    pen.penup()
    pen.getscreen().tracer(1000,0)
    if r < 1:
        x = 0
        y = 0.16*y
    elif r < 86:
        x =  0.85*x + 0.04*y
        y = -0.04*x + 0.85*y + 1.6
    elif r < 93:
        x =  0.20*x - 0.26*y
        y =  0.23*x + 0.22*y + 1.6
    else:
        x = -0.15*x + 0.28*y
        y =  0.26*x + 0.24*y + 0.44
   


