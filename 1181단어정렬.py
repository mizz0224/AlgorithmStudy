count = int(input())
arr = list()
arr2 = list()
for _ in range(count):
    get_st = input()
    if get_st not in arr:
        arr.append(get_st)

arr.sort()
arr.sort(key=len)
# for ord in range(1, 51):
#     arr3 = list()
#     for word in arr:
#         if len(word) == ord and word not in arr3:
#             arr3.append(arr.pop(arr.index(word)))
#     arr3.sort()
#     arr2 += arr3
for wrd in arr:
    print(wrd)
