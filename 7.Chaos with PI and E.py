import turtle
import math

pen = turtle.Turtle()
pen.speed(0)
pen.getscreen().tracer(100,0)

i = 0

while True:
    i=i+1
    pen.forward(math.sqrt(i))
    pen.left(math.pi*i*math.e)
    
    
    



