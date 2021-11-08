print_count = int(input())
count_arr = list()
for _ in range(print_count):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_dic = dict()
    count = 0
    if len(arr) == 1:
        pass
    else:
        while True:
            big = False
            for i in range(1, len(arr)):
                if arr[i] > arr[0]:
                    big = True
            if m == 0 and big == False:
                break
            if big:
                arr.append(arr.pop(0))
                if m == 0:
                    m = len(arr) - 1
                else:
                    m -= 1
            else:
                arr.pop(0)
                count += 1
                m -= 1

    count_arr.append(count + 1)

for i in count_arr:
    print(i)
