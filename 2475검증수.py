arr = list(map(int, input().split()))
for i in range(len(arr)):
    arr[i] = arr[i] * arr[i]
sum = sum(arr)
print(sum % 10)
