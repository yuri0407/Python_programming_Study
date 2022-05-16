from myTurtle import *
import turtle as t

inStr = ""
swidth, sheight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

t.title("거북이 글자쓰기(모듈버전)")
t.shape("turtle")
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.speed(5)

inStr = getString()

for ch in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    t.goto(tX, tY)
    t.left(tAngle)

    t.pencolor((r, g, b))
    t.write(ch, font = ("맑은고딕", txtSize, "bold"))

t.done()