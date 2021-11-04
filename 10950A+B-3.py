count = int(input())
arr = list()
for _ in range(count):
    a, b = map(int, input().split())
    arr.append(a + b)
for i in arr:
    print(i)
