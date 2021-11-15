import sys

n = int(sys.stdin.readline())
arr = list()
for _ in range(n):
    input_check = False
    get_num = int(sys.stdin.readline())
    i = -1
    if len(arr) < 2:
        arr.append(get_num)
        input_check = True
    else:
        i = 0
        j = len(arr) - 1
        mid = i + j // 2
        while j - i > 1:
            mid = i + j // 2
            if arr[mid] == get_num:
                break
            elif arr[mid] > get_num:
                i = mid
            else:
                j = mid
        arr.insert(mid + 1, get_num)
        input_check = True
    # if input_check == False:
    #    arr.append(get_num)
for i in arr:
    print(i)
