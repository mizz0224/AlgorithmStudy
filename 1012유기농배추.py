import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def clean(x, y):
    queue = list()
    queue.append([x, y])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and ground[q][w] == 1:
                ground[q][w] = 0
                queue.append([q, w])


answer_arr = list()
count = int(sys.stdin.readline())
for _ in range(count):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    ground = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1
    for d in range(n):
        for w in range(m):
            if ground[d][w] == 1:
                clean(d, w)
                count += 1
    answer_arr.append(count)

for answer in answer_arr:
    print(answer)
