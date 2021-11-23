import sys

count = int(sys.stdin.readline())
arr = list()
for _ in range(count):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
    print(i)
