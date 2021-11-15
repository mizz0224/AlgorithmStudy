import sys


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm(a, b):
    l = a * b
    for i in range(max(a, b), l + 1):
        if i % a == 0 and i % b == 0:
            l = i
            break
    return l


n, m = map(int, sys.stdin.readline().split())
print(gcd(n, m))
print(lcm(n, m))
