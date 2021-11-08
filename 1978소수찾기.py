count = input()
num_arr = list(map(int, input().split()))
start = min(num_arr)
end = max(num_arr)
is_prime = [True] * (end + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(end ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, end + 1, i):
            is_prime[j] = False
count = 0
for i in range(start, end + 1):
    if is_prime[i] and i in num_arr:
        count += 1
print(count)
