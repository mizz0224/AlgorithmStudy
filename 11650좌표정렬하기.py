import sys

count = int(sys.stdin.readline())
arr = dict()
for _ in range(count):
    x, y = map(int, sys.stdin.readline().split())
    if x in arr.keys():
        arr[x].append(y)
    else:
        arr[x] = [y]

for x, y in sorted(arr.items()):
    y.sort()
    for y1 in y:
        print(str(x) + " " + str(y1))
