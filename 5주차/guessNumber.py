import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오.")

while guess != answer:
    guess = int(input("숫자를 입력하세요 : "))
    tries = tries + 1
    if tries == 10:
        break
    elif guess < answer:
        print("정답보다 숫자가 낮습니다.")
    elif guess > answer:
        print("정답보다 숫자가 높습니다.")

if guess == answer:
    print("축하합니다. 시도횟수 = ", tries)
else:
    print("정답은 %d입니다." % answer)