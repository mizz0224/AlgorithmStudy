import sys

answer_list = list()
while True:
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == line[1] == line[2] and line[0] == 0:
        break
    longest = line.pop(line.index(max(line)))
    if longest ** 2 == line[0] ** 2 + line[1] ** 2:
        answer_list.append("right")
    else:
        answer_list.append("wrong")

for answer in answer_list:
    print(answer)
