import sys

n = int(sys.stdin.readline())
for i in range(1, 1000001):
    num = i
    st = str(i)
    for s in st:
        num += int(s)
    if num == n:
        print(i)
        break
if i == 1000000:
    print("0")