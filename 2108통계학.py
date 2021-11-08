import sys

count = int(sys.stdin.readline())
arr = list()
arr_dic = dict()
sum = 0
mid = round(count // 2)
for _ in range(count):
    num = int(sys.stdin.readline())
    arr.append(num)
    sum += num
    if num in arr_dic.keys():
        arr_dic[num] += 1
    else:
        arr_dic[num] = 1
print(round(sum / count))
arr.sort()
print(arr[mid])
key_arr = list()
max_value = sorted(arr_dic.values())[-1]
for key, value in arr_dic.items():
    if value == max_value:
        key_arr.append(key)
if len(key_arr) > 1:
    key_arr.sort()
    print(key_arr[1])
else:
    print(key_arr[0])

print(arr[-1] - arr[0])
