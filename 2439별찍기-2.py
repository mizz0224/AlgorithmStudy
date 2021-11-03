count = int(input())
for i in range(1, count + 1):
    empty = count - i
    st1 = " " * empty
    st2 = "*" * i
    print(st1 + st2)
