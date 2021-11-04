st = list(input())
alphabet_list = list()
st_toprint = ""
for i in range(97, 123):
    alphabet_list.append(chr(i))
for chr in alphabet_list:
    if chr in st:
        st_toprint += str(st.index(chr))
    else:
        st_toprint += "-1"
    st_toprint += " "
print(st_toprint)
