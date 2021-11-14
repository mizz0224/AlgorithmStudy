import sys

target = int(sys.stdin.readline())
start = 1
finish = 1
for i in range(target):
    if i != 0:
        start = finish + 1
        finish += 6 * i
    if target >= start and target <= finish:
        print(i+1)
        break

# 1
# 2~7 : 6
# 8~19 : 12
#
#
