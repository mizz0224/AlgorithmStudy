arr = list()
for _ in range(10):
    num = int(input())
    nam = num % 42
    if nam in arr:
        pass
    else:
        arr.append(nam)
print(len(arr))
