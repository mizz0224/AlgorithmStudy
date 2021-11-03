get_count = int(input())
arr = list()
for _ in range(get_count):
    st = ""
    count, get_st = input().split()
    for ch in get_st:
        st += ch * int(count)
    arr.append(st)
for i in arr:
    print(i)
