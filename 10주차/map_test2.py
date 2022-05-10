myList = [1, 2, 3, 4, 5]
result1 = []
for val in myList:
    result1.append(val + 1)
print(result1)

def add_one(n):
    return n + 1;

#map반환을 list로 변환
result2 = tuple(map(add_one, myList))
print(result2)