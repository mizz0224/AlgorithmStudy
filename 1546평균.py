count = int(input())
arr = list(map(int, input().split()))
sum = 0
for a in arr:
    sum += a
sum /= count
sum *= 100
print(sum / max(arr))
