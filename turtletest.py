import turtle
t = turtle.Turtle()

t.color('green', 'yellow')
t.begin_fill()

def create_square():
    t.pendown
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

    t.end_fill

create_square()

turtle.done()     