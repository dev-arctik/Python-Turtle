#Factral tree

from turtle import Turtle, mainloop
import turtle
import random



def tree(plist, l, a, n):
    pen = []
    if l > 1.5:
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            pen.append(p)
            pen.append(q)
        for x in tree(pen, l*n, a, n):
            yield None


def start():
    p = Turtle()
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(100,0)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    n = random.random()
    print (n)
    a = random.randrange(1,90)
    print (a)
    t = tree([p], 200, 65, 0.637)  #for a proper factral tree change a to 65 and n to 0.63
    for x in t:
        pass

start()

print("Close or click on turtle window to complete exit")
turtle.exitonclick()

