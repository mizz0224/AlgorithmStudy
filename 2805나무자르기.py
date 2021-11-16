import sys

tree_count, target = map(int, sys.stdin.readline().split())
tree_arr = list(map(int, sys.stdin.readline().split()))
end = max(tree_arr)
start = 1
while start <= end:
    mid = (start + end) // 2
    amount = 0
    for tree in tree_arr:
        if tree > mid:
            amount += tree - mid

    if amount >= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)
