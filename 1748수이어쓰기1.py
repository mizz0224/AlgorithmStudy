import sys

n = sys.stdin.readline().strip()
count_of_ten = len(n) - 1
count = 0
nine = 1
for i in range(count_of_ten):
    count += 9 * (10 ** i) * (i + 1)
count += ((int(n) - (10 ** count_of_ten)) + 1) * (count_of_ten + 1)
print(count)
