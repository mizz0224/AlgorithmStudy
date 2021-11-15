import sys

n = int(sys.stdin.readline())
answer_arr = list()
for _ in range(n):
    floor = int(sys.stdin.readline())
    unit = int(sys.stdin.readline())
    arr = list()
    f_0 = list()
    for u in range(unit + 1):
        f_0.append(u)
    arr.append(f_0)
    for f in range(1, floor + 1):
        f_arr = [0]
        for u in range(1, unit + 1):
            num = 0
            for i in range(u + 1):
                num += arr[f - 1][i]
            f_arr.append(num)
        arr.append(f_arr)
    answer_arr.append(arr[floor][unit])
for i in answer_arr:
    print(i)
