import sys

n = int(sys.stdin.readline())
answer_list = list()
answer_list.append(n)
for i in range((n // 5) + 1):
    amount = n
    count = 0
    five_kilo = i * 5
    if five_kilo > amount:
        pass
    else:
        count += i
        amount -= five_kilo
        for j in range((amount // 3) + 1):
            three_kilo = j * 3
            if amount == three_kilo:
                count += j
                answer_list.append(count)


min = min(answer_list)
if min == n:
    print(-1)
else:
    print(min)
