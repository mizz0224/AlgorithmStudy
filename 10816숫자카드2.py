import sys

have_count = int(sys.stdin.readline())
have_arr = list(map(int, sys.stdin.readline().split()))
have_dic = dict()
for i in have_arr:
    if i in have_dic.keys():
        have_dic[i] += 1
    else:
        have_dic[i] = 1
get_count = int(sys.stdin.readline())
get_arr = list(map(int, sys.stdin.readline().split()))
s = ""
for i in get_arr:
    if i in have_dic.keys():
        s += str(have_dic[i]) + " "
    else:
        s += "0" + " "

print(s.rstrip())
