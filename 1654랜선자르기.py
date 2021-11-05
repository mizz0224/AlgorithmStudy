# have, want = map(int, input().split())
# arr = list()
# for _ in range(have):
#     arr.append(int(input()))
# low = 0
# high = 10000000
# while low <= high:
#     count = 0
#     mid = (low + high) // 2
#     for i in arr:
#         count += i // mid
#     if count >= want:
#         low = mid + 1
#     else:
#         high = mid - 1

# print(high)
