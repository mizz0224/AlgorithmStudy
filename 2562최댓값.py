max_num = 0
max_count = 0
for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        max_count = i
print(max_num)
print(max_count)
