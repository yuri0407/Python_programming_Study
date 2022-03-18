import turtle as t

t.shape('turtle');
t.speed(0)
t.pensize(20)

t.circle(100)               # 중앙에 있는 검은색 원을 먼저 그린다.

t.up()
t.fd(240)                   # 앞으로 240만큼 이동한다. (오른쪽 원을 그리기 위해)
t.down()
t.pencolor('red')           # 빨간색 원을 그린다.
t.circle(100)

t.up()
t.backward(480)             # 뒤로 480만큼 이동한다. (왼쪽 원을 그리기 위해)
t.down()
t.pencolor('blue')          # 파란색 원을 그린다.
t.circle(100)

t.up()
t.rt(90)                    # 먼저 밑으로 120만큼 가기 위해 오른쪽으로 90도 회전한다. (나중에 위치 잡기 편하도록)
t.fd(120)
t.lt(90)                    # 옆으로 가기 위해 왼쪽으로 90도 회전한다.
t.fd(120)
t.down()
t.pencolor('yellow')        # 노란색 원을 그린다.
t.circle(100)

t.up()
t.fd(240)                   # 앞으로 240만큼 이동한다.
t.down()
t.pencolor('green')         # 초록색 원을 그린다.
t.circle(100)


t.done()
