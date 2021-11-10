# import sys

# for n in range(2, 101):
#     arr = list()
#     for i in range(1, n + 1, 2):
#         arr.append(i + 1)
#     while len(arr) > 1:
#         arr.pop(0)
#         arr.append(arr.pop(0))
#     print(n, arr[0])
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()
for i in range(n):
    arr.append(i + 1)
while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
print(arr.pop())
