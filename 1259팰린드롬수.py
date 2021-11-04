arr = list()
while True:
    st = input()
    if st == "0":
        break
    else:
        result = "yes"
        for i in range(len(st) // 2):
            if st[i] != st[-(i + 1)]:
                # len(st) -
                result = "no"
        arr.append(result)
for result in arr:
    print(result)
