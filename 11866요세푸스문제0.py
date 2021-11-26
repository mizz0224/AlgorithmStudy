import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(range(1, n + 1))
answer_arr = list()
k -= 1
index = k
while len(arr) > 0:
    try:
        while index >= len(arr):
            index -= len(arr)
        answer_arr.append(arr.pop(index))
        index += k
    except:
        print(arr)
print("<" + str(answer_arr).lstrip("[").rstrip("]") + ">")
