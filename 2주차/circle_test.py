import turtle as t

c = int(input("몇 개의 원을 그릴까요? : "))
t.shape('turtle')
t.speed(50)

for i in range(c):
    t.circle(100)
    t.fd(15)

t.done()