import sys

round = dict()
answer = dict()
n, m, b = map(int, sys.stdin.readline().split())
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for i in line:
        if i in round.keys():
            round[i] += 1
        else:
            round[i] = 1
mi = min(round.keys())
mx = max(round.keys())
min_count = 9999999999999999999
high = 0
for i in range(mi, mx + 1):  # i : 기준이 될것
    count = 0
    block = b
    for j in round.keys():
        if i > j:
            count += (i - j) * round[j]
            block -= (i - j) * round[j]
        elif i < j:
            count += 2 * (j - i) * round[j]
            block += (j - i) * round[j]
    if block > -1:
        min_count = min(min_count, count)
        if min_count == count:
            h = i

print(min_count, h)
