print_count = int(input())
count_arr = list()
for _ in range(print_count):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_dic = dict()
    count = 0
    while True:
        print(arr)
        count += 1
        if len(arr) == 1:
            break
        big = False
        for i in range(1, len(arr)):
            if arr[i] > arr[0]:
                big = True
        if big:
            arr.append(arr.pop(0))
            if m == 0:
                m = len(arr) - 1
            else:
                m -= 1
        else:
            arr.pop(0)
            m -= 1
        if m == 0:
            break
    count_arr.append(count)

for i in count_arr:
    print(i)
