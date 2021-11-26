import sys

count = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
answer = 0
for i in range(len(arr)):
    alphabet_to_int = ord(arr[i]) - 96
    answer += alphabet_to_int * 31 ** i
print(answer % 1234567891)
