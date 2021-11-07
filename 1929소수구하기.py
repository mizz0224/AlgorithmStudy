start, end = map(int, input().split())
is_prime = [True] * (end + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(end ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, end + 1, i):
            is_prime[j] = False
for i in range(start, end + 1):
    if is_prime[i]:
        print(i)
