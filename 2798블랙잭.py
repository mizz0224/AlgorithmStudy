import sys

card_count, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)
answer_arr = list()
for i in range(card_count):
    for j in range(i + 1, card_count):
        for k in range(j + 1, card_count):
            add = arr[i] + arr[j] + arr[k]
            if add <= target:
                answer_arr.append(add)
print(max(answer_arr))
