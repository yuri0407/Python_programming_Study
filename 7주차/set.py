mySet1 = {1, 2, 3, 3, 3, 4}
print("mySet1 =", mySet1)

#=====================================================

salesList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
set(salesList)

#=====================================================

Set1 = {1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7}

Set1 & Set2
Set1 | Set2
Set1 - Set2
Set1 ^ Set2

#=====================================================

numList = []

for num in range(1, 6):
    numList.append(num)

print("numList =", numList)

#=====================================================

numList2 = [num for num in range(1, 6)]
print("numList2 =", numList2)

#=====================================================

foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']

print("===========================")
for food, side in zip(foods, sides):
    print(food, '==>', side)

#=====================================================

a = ['one', 'two', 'three']
b = ['a', 'b', 'c']
for val1, val2, in zip(a, b):
    print(val1, val2)

#=====================================================

A = ['name', 'age', 'phone', 'gender']
B = ['CHAN', 28, '010-xxxx-yyyy', 'male']
d = dict(zip(A, B))

#=====================================================

a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3]

print("===========================")
for s in zip(a, b):
    print(s)
    print(list(s))

#=====================================================

foods2 = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides2 = ['오뎅', '단무지', '김치']
tupList = list(zip(foods2, sides2))
dic = dict(zip(foods2, sides2))

print("===========================")

print(tupList)
print(dic)

#=====================================================

oldList = ['짜장면', '탕수육', '군만두']
newList = oldList

print("===========================")

print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)

#=====================================================

oldList2 = ['짜장면', '탕수육', '군만두']
newList2 = oldList2[:]

print("===========================")

print(newList2)
oldList2[0] = '짬뽕'
oldList2.append('깐풍기')
print(newList2)