def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    a = input("첫 번째 숫자를 입력하세요 : ")

    #입력한 첫번째 숫자값이 "000"일 경우 두 번째 숫자는 입력받지 않고 즉시 프로그램 종료
    if a == "000":
        break
    else:
        a = int(a)
        b = int(input("두 번째 숫자를 입력하세요 : "))

    print(a, "+", b, "=", add(a, b))
    print(a, "-", b, "=", minus(a, b))
    print(a, "*", b, "=", multi(a, b))
    print(a, "/", b, "=", divide(a, b))
