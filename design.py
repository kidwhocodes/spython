import turtle as t
import random as r
t.speed(10)

#all designs
def Portal():
    for i in range(100):
        t.forward(200)
        t.left(145)
def Crazy1():
    for i in range(90):
        t.left(r.randrange(70, 140))

design = input("Which design would you like. Portal, Star, Crazy1, or Crazy2. When you type which design you want, please make sure you type the design correctly.\n")
if design == "Portal":
    Portal()
elif design == "Crazy1":
    Crazy1()