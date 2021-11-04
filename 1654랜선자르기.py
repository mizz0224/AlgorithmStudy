have, want = map(int, input().split())
arr = list()
for _ in range(have):
    arr.append(int(input()))
mx = max(arr)
check = True
while check:
    for i in range(mx, 0, -1):
        count = 0
        for j in arr:
            count += j // i
        if count >= want:
            print(i)
            check = False
            break
