import turtle
import random
pen = turtle.Turtle()
pen.pensize(0.5)
pen.speed(0)
pen.color('black')
pen.hideturtle()

#a
x1=0
y1=250
pen.penup()
pen.setpos(x1,y1)
pen.pendown()
pen.dot()
pen.penup()


#b
x2=-250
y2=-250
pen.setpos(x2,y2)
pen.pendown()
pen.dot()
pen.penup()


#c
x3=250
y3=-250
pen.setpos(x3,y3)
pen.pendown()
pen.dot()
pen.penup()


x=random.randrange(-250,250)
y=random.randrange(-250,250)
pen.setpos(x,y)
pen.pendown()
pen.dot()
pen.penup()
print('{},{}'.format(x,y))
for i in range(2000000000000000000000):
    print (i)
    pnt = random.choice(['a', 'b', 'c'])
    print(pnt)

    if (pnt=='a'):
        x = (x+x1)/2
        y = (y+y1)/2
    elif (pnt=='b'):
        x = (x+x2)/2
        y = (y+y2)/2
    elif (pnt=='c'):
        x = (x+x3)/2
        y = (y+y3)/2
    pen.setpos(x,y)
    print('{},{}'.format(x,y))
    pen.pendown()
    pen.dot()
    pen.penup()
    pen.getscreen().tracer(100,0)

v
