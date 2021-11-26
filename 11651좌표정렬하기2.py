import sys

count = int(sys.stdin.readline())
arr = dict()
for _ in range(count):
    x, y = map(int, sys.stdin.readline().split())
    if y in arr.keys():
        arr[y].append(x)
    else:
        arr[y] = [x]

for x, y in sorted(arr.items()):
    y.sort()
    for y1 in y:
        print(str(y1) + " " + str(x))
