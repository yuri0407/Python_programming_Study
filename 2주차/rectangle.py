import turtle as t

t.pensize(4)
t.color('blue')
t.bgcolor('yellowgreen')
t.fillcolor('skyblue')

t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()

t.done()