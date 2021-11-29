import sys

dogam = dict()
answer = list()
count, question = map(int, sys.stdin.readline().split())
for i in range(count):
    dogam[i] = sys.stdin.readline().rstrip()
dogam_reverse = dict(map(reversed, dogam.items()))
for _ in range(question):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        answer.append(dogam[int(q) - 1])
    else:
        answer.append(dogam_reverse[q] + 1)

for a in answer:
    print(a)
