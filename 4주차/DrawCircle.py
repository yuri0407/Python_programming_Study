import random
import turtle as t

t.shape("turtle")
t.pensize(5)

def randomDrawCircle(x, y):
    t.color("red")
    for i in range(0, 50):
        rX = random.randrange(-600, 600)
        rY = random.randrange(-600, 600)
        t.penup()
        t.goto(rX, rY)
        t.pendown()
        t.circle(50)

t.onscreenclick(randomDrawCircle, 1)

t.done()