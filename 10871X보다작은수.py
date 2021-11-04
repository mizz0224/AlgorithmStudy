a, standard = map(int, input().split())
arr = list(map(int, input().split()))
st = list()
for i in arr:
    if i < standard:
        st.append(str(i))

print(" ".join(st))
