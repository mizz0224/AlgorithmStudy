count = int(input())
arr = list()
for _ in range(count):
    st = input()
    ocount = 0
    osum = 0
    for s in range(len(st)):
        if st[s] == "O":
            ocount += 1
        else:
            ocount = 0
        osum += ocount
    arr.append(osum)
for i in arr:
    print(i)
