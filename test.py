# def ca(n):
#     arr = list()
#     arr.append(0)
#     for i in range(1, n + 1):
#         if i == 1:
#             arr.append(1)
#         elif i == 2:
#             arr.append(1)
#         else:
#             if i % 2 == 1:
#                 arr.append(arr[i - 1] + arr[i - 2])
#             else:
#                 arr.append(arr[i - 1] - arr[i - 2])

#     return arr


# print(ca(32))
# max = 0
# for i in range(6, 127):
#     count_1 = str(bin(i)).count("1")
#     if max < count_1:
#         max = count_1
# for i in range(6, 127):
#     count_1 = str(bin(i)).count("1")
#     if max == count_1:
#         print(i)
#         break

n = int(input())
arr = list(map(int, input().split()))
arr2 = list()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k and arr[i] < arr[j] and arr[i] > arr[k]:
                line = [i + 1, j + 1, k + 1]
                if line not in arr2:
                    arr2.append(line)
print(arr2)
print(len(arr2))
