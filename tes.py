arr = dict()
sum = 0
for i in range(1, 30):
    arr[i] = 300000
for key, value in arr.items():
    money = value
    if key // 12 > 0:
        for _ in range((key) // 12):
            money *= 1.027
    arr[key] = money
    sum += money
print(sum)
print(arr)
