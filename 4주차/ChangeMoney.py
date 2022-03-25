money = int(input("교환할 돈은 얼마? "))

m500 = money // 500
money %= 500

m100 = money // 100
money %= 100

m50 = money // 50
money %= 50

m10 = money // 10
money %= 10

print("500원짜리 ==> %d개" % m500)
print("100원짜리 ==> %d개" % m100)
print("50원짜리 ==> %d개" % m50)
print("10원짜리 ==> %d개" % m10)
print("바꾸지 못한 잔돈 ==> %d원" % money)
