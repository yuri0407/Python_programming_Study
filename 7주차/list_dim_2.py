aa = [[1, 2, 3, 4],
      [5, 6],
      [7, 8, 9]]

totalSum = 0

for i in range(len(aa)):
    sum = 0
    for j in range(len(aa[i])):
        sum += aa[i][j]
    print(sum)
    totalSum += sum

print("total:", totalSum)