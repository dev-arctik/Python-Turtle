import turtle
pen = turtle.Turtle()
pen.pensize(1)
pen.color('black')
pen.penup()
pen.setpos(0,-275)
pen.pendown()
pen.speed(0)
pen.hideturtle()

for j in range (3,2000):
    print('Number of sides: {}' .format(j))
    a=(360/j)
    print('Angle of each side: {}'.format(a/2))
    for i in range (j):
        pen.forward(75)
        pen.left(a)
        pen.getscreen().tracer(100,0)


