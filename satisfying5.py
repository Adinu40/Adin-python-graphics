from turtle import *
bgcolor('blue')
width(3)
hideturtle()
speed(15)
color('red', 'yellow')
begin_fill()
while True:
    forward(500)
    circle(20)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()