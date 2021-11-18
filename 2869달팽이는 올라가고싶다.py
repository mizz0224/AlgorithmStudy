import sys

a, b, v = map(int, sys.stdin.readline().split())

one_day = a - b
day = v / one_day
if day > v // one_day:
    day = v // one_day + 1
else:
    day = v // one_day
print(day)
