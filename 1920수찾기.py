import sys

n_count = int(sys.stdin.readline().rstrip())
narr = list(map(int, sys.stdin.readline().split()))
m_count = int(sys.stdin.readline().rstrip())
marr = list(map(int, sys.stdin.readline().split()))
narr.sort()
for i in marr:
    low = 0
    high = n_count - 1
    find = False
    while low <= high:
        mid = (low + high) // 2
        if narr[mid] == i:
            find = True
            break
        elif narr[mid] > i:
            high = mid - 1
        else:
            low = mid + 1
    print(int(find))
