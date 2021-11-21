import sys

case_count = int(sys.stdin.readline())
answer_arr = list()
for _ in range(case_count):
    h, w, n = map(int, sys.stdin.readline().split())
    unit = n // h

    floor = n - (h * unit)
    if floor == 0:
        floor = h
    if n // h < n / h:
        unit += 1
    if unit < 10:
        unit = "0" + str(unit)
    else:
        unit = str(unit)
    answer = str(floor) + unit
    answer_arr.append(answer)
for answer in answer_arr:
    print(answer)
