import sys

for n in range(2, 101):
    arr = list()
    for i in range(1, n + 1, 2):
        arr.append(i + 1)
    while len(arr) > 1:
        arr.pop(0)
        arr.append(arr.pop(0))
    print(n, arr[0])
