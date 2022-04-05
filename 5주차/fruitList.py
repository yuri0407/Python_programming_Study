j = 0
fruit = ['apple', 'banana', 'mango', 'melon']
fruit.append('strawberry')
print(len(fruit))
fruit.pop()
print(len(fruit))
fruit.pop()
print(len(fruit))

for i in fruit:
    print(fruit.index(i), i)

    if 'apple' in fruit:        #'apple'이 fruit 배열 안에 포함되어 있다면 'buy'출력, 아니면 'not buy'출력
        print('buy')
    else:
        print('not buy')
    # fruit.index(i)
    # print("Hello")
    # print(j, fruit[j])
    # j = j + 1
    # print(fruit[0])
    # print(i)
