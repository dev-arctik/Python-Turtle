import turtle


pen = turtle.Turtle()
pen.color("red")
pen.speed(0)
pen.up()
pen.backward(100)
pen.down()

for i in range(36):
    pen.begin_fill()
    pen.forward(200)
    pen.left(170)
    pen.end_fill()


