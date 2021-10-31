count = int(input())
for i in range(count):
    if i == 0:
        s = list(input())
    else:
        s2 = list(input())
        for index in range(len(s)):
            if s[index] != s2[index]:
                s[index] = "?"
print("".join(s))
