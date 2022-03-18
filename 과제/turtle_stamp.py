# 모듈 가져오기
import turtle as t
import random

# 함수 생성하기
def ScreenLeftClick(x, y):
    tSize = random.randrange(2, 10)     # 거북이의 크기가 2에서 10까지 랜덤으로 지정됨
    t.shapesize(tSize)

    r = random.random()                 # 색 코드(RGB)가 랜덤으로 지정됨
    g = random.random()
    b = random.random()

    t.color((r, g, b))                  # 지정된 코드를 거북이 색으로 지정
    tAngle = random.randrange(0, 360)   # 거북이가 향할 각도가 0도에서 360도까지의 범위에서 랜덤으로 지정됨

    t.penup()
    t.goto(x, y)                        # 함수를 호출할 때 입력받은 좌표 값으로 거북이가 이동
    t.lt(tAngle)                        # 지정된 각도만큼 왼쪽으로 회전함
    t.stamp()

#메인 코드
pSize = 10                              # 필요한 변수들을 초기화시킴
r, g, b = 0.0, 0.0, 0.0

t.title('거북이 도장 찍기')             # 실행시키면 뜨는 창의 제목 지정
t.shape('turtle')

t.onscreenclick(ScreenLeftClick, 1)     # 마우스 왼쪽을 클릭하면 생성한 함수가 실행

t.done()
