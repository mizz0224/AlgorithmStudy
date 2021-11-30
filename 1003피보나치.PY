import sys

zero = [1, 0, 1]
one = [0, 1, 1]
answer = list()


def fibonacci(n):
    zero_len = len(zero)
    if n >= zero_len:
        for i in range(zero_len, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    return str(zero[n]) + " " + str(one[n])


count = int(sys.stdin.readline())
for _ in range(count):
    num = int(sys.stdin.readline())
    answer.append(fibonacci(num))

for a in answer:
    print(a)
