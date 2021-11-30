import sys

count = int(sys.stdin.readline())
for _ in range(count):
    row, column, cabbage_count = map(int, sys.stdin.readline().split())
    bat = list()
    for i in range(column):
        line = list()
        for j in range(row):
            line.append(0)
        bat.append(line)
    for _ in range(cabbage_count):
        x, y = map(int, sys.stdin.readline().split())
        bat[y][x] = 1
    for l in bat:
        print(l)
