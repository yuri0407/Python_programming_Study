import turtle as t
import random

swidth, sheight = 500, 500

t.title("무지개색 원 그리기")
t.shape("turtle")
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.goto(0, -sheight / 2)
t.pendown()
t.speed(15)

for radius in range(1, 250):
    r = random.random()
    g = random.random()
    b = random.random()

    t.pencolor((r, g, b))
    t.circle(radius)

t.done()