def bridge_count(n, m):
    for i in range(1,n):
        for j in range (1,m):


case_count = int(input())

for _ in range(case_count):
    n, m = map(int, input().split())
    bridge_count(n, m)
