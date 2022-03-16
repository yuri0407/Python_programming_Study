import turtle as t

h = int(input("Enter the height of the Rectangle: "))
w = int(input("Enter the width of the Rectangle: "))

for i in range(4):
    if i%2 == 0:
        t.fd(h)
        t.lt(90)
    else:
        t.fd(w)
        t.lt(90)

t.done()