arr = list()
while True:
    a, b = map(int, input().split())
    if a + b != 0:
        arr.append(a + b)
    else:
        break
for i in arr:
    print(i)
