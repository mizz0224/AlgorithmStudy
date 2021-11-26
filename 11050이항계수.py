import sys


def fact(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


n, k = map(int, sys.stdin.readline().split())

print(fact(n) // fact(n - k) // fact(k))
