import sys

arr = list()
count_num = int(sys.stdin.readline())

for _ in range(count_num):
    line = list(sys.stdin.readline().rstrip().split())
    age = int(line[0])
    name = line[1]
    line = [age, name]
    if len(arr) == 0:
        arr.append(line)
    elif len(arr) == 1:
        if arr[0][0] > age:
            arr.insert(0, line)
        else:
            arr.insert(1, line)
    else:
        index = -1
        while arr[index] != arr[0]:
            if arr[index][0] < age:
                arr.insert(arr.index(arr[index]) + 1, line)
                break
            else:
                index -= 1
        if arr[index] == arr[0]:
            if arr[0][0] > age:
                arr.insert(0, line)
            else:
                arr.insert(1, line)
for p in arr:
    s = str(p[0]) + " " + str(p[1])
    print(s)
