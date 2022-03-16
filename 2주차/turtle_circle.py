import turtle as t

t.shape('turtle')
t.color('pink')
t.speed(100)

r = int(input("몇 개의 원을 그릴까요? :"))

for i in range(r):
    t.circle(100)
    t.lt(360/r)
    t.fd(20)

t.done()
