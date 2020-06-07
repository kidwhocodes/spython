import turtle as t

t.bgcolor('white')
t.goto(0,0)
def  move_up():
    t.setheading(90)
    t.forward(20)
def move_right():
    t.setheading(180)
    t.forward(20)

t.listen()
t.mainloop()