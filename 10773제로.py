import sys

count = int(sys.stdin.readline())
money_arr = list()
total = 0
for _ in range(count):
    money = int(sys.stdin.readline())
    if money == 0:
        total -= money_arr.pop()
    else:
        money_arr.append(money)
        total += money

print(total)
