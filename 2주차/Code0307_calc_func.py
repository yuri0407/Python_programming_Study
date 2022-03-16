def add(a, b):
    c = a + b
    return c

def minus(a, b):
    c = a - b
    return c

def multi(a, b):
    c = a * b
    return c

def divide(a, b):
    c = a / b
    return c

while True:
    a = input("첫 번째 숫자를 입력하세요: ")

    #입력한 첫번째 숫자값이 "000"일 경우 두 번째 숫자는 입력받지 않고 즉시 프로그램 종료
    if(a == "000"):
        break
    else:
        a = int(a)
        b = int(input("두 번째 숫자를 입력하세요: "))

    result = add(a, b)
    print(a, "+", b, "=", result)

    result = minus(a, b)
    print(a, "-", b, "=", result)

    result = multi(a, b)
    print(a, "*", b, "=", result)

    result = divide(a, b)
    print(a, "/", b, "=", result)
    
print("end of program")
