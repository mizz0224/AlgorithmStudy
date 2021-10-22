import sys

arr = list()
st = ""
while True:
    try:
        getst = input()
        if getst == -1:
            break
        else:
            for i in getst.split():
                i = i[::-1]
                arr.append(int(i))
                # arr.append(int(reversed(i)))
    except EOFError:
        break
del arr[0]
arr.sort()
for i in arr:
    print(i)
