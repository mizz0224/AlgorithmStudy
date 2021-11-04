x, y, w, h = map(int, input().split())
rectangle = [0, 0, w, h]
arr = list()
for i in range(4):
    if i % 2 == 0:
        if rectangle[i] - x < 0:
            arr.append(-(rectangle[i] - x))
        else:
            arr.append((rectangle[i] - x))
    else:
        if rectangle[i] - y < 0:
            arr.append(-(rectangle[i] - y))
        else:
            arr.append((rectangle[i] - y))

print(min(arr))
