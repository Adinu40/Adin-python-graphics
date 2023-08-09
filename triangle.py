from turtle import *


width(20)


def draw_triangle(linecolor, length=50):
    color(linecolor)
    begin_fill()
    for i in range(3):
        forward(length)
        left(120)
    end_fill()


draw_triangle('red')
right(180)
forward(100)
right(180)
draw_triangle('green', 100)
right(180)
forward(200)
right(180)
draw_triangle('blue', 200)

done()
turtle.done()

