import turtle as t

t.shape('turtle')

for i in range(20):
    t.fd(200 + i * 10)
    t.rt(90 + i * 5)

t.done()