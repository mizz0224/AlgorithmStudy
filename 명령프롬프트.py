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
# n = int(input())
# a = list(input())
# a_len = len(a)
# for i in range(n - 1):
#     b = list(input())
#     for j in range(a_len):
#         if a[j] != b[j]:
#             a[j] = "?"
# print("".join(a))
