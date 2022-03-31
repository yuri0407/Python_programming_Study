score = int(input("점수를 임력하세요 : "))

if score >= 95:
    print("A+학점입니다.")
elif score >= 90:
    print("A학점입니다.")
elif score >= 85:
    print("B+학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 75:
    print("C+학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 65:
    print("D+학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")