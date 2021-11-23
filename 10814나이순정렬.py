import sys

arr = dict()
count_num = int(sys.stdin.readline())

for _ in range(count_num):
    line = list(sys.stdin.readline().rstrip().split())
    age = int(line[0])
    name = line[1]
    line = [age, name]
    if age in arr.keys():
        arr[age] = arr[age] + [name]
    else:
        arr[age] = [name]

for key, value in sorted(arr.items()):
    for v in value:
        print(str(key) + " " + str(v))
