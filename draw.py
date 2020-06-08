import turtle as t

t.bgcolor('black')
t.color('white')
t.goto(0,0)

def  move_up():
    t.setheading(90)
    t.forward(20)

def move_right():
     t.setheading(0)
     t.forward(20)
   
def move_down():
    t.setheading(-90)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def Z():
    t.penup()

def X():
    t.pendown()

def Space():
    t.undo()

t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(Z,'z')
t.onkey(X,'x')
t.onkey(Space,'space')

t.listen()
t.mainloop()