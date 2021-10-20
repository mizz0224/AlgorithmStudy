s = input()
dic = dict()

s = s.upper()
for i in s:
    if i >= "A" and i <= "Z":
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

maxcount = 0
maxkey = "?"
many = False
for key, value in dic.items():
    if value > maxcount:
        maxcount = value
        maxkey = key
        many = False
    elif value == maxcount:
        many = True


print("?" if many else maxkey)

import sys

word = list((sys.stdin.readline().rstrip()).upper())
dt = dict()

for i in word:
    dt[i] = dt.get(i, 0) + 1

maxcnt = 0
maxkey = "?"

for k, v in dt.items():
    if v > maxcnt:
        maxcnt = v
        maxkey = k
    elif v == maxcnt:
        maxkey = "?"

print(maxkey)
