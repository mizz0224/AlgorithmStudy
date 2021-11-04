index = int(input())
num = 0
arr = list()
while True:
    if "666" in str(num):
        arr.append(num)
        if len(arr) == index:
            print(num)
            break
    num += 1
