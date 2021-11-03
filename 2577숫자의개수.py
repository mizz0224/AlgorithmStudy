num = 1
for i in range(3):
    num *= int(input())
st = str(num)
for i in range(10):
    print(st.count(str(i)))
