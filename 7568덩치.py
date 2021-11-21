import sys

count_num = int(sys.stdin.readline())
arr = list()
for order in range(count_num):
    weight, hight = map(int, sys.stdin.readline().split())
    person = [weight, hight, 1]
    arr.append(person)


for i in range(len(arr)):
    person = arr.pop(i)
    weight = person[0]
    hight = person[1]
    order = person[2]
    for other in arr:
        if weight < other[0] and hight < other[1]:
            order += 1
    arr.insert(i, [weight, hight, order])
st = ""
for person in arr:
    st += str(person[2])
    st += " "
print(st.rstrip())
