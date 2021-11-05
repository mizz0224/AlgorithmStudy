import sys

cut, student = map(int, sys.stdin.readline().split())
arr = dict()
order = 0
for _ in range(student):
    student_num = sys.stdin.readline().rstrip()
    arr[student_num] = order
    order += 1
count = 0
for key, value in sorted(arr.items(), key=lambda value: value[1]):
    count += 1
    print(key)
    if count == cut:
        break
