import sys

count = int(sys.stdin.readline())
arr = dict()
for _ in range(count):
    num = int(sys.stdin.readline())
    if num in arr.keys():
        arr[num] += 1
    else:
        arr[num] = 1

for key, value in sorted(arr.items()):
    for _ in range(value):
        print(key)
