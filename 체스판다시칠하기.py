column, row = map(int, input().split())
arr = list()
countarr = list()
for _ in range(column):
    arr.append(list(input()))
for i in range(column - 7):
    for j in range(row - 7):
        countB = 0
        countW = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if arr[k][l] != "W":
                        countW += 1
                    else:
                        countB += 1
                else:
                    if arr[k][l] != "B":
                        countW += 1
                    else:
                        countB += 1
        countarr.append(min(countW, countB))
print(min(countarr))
