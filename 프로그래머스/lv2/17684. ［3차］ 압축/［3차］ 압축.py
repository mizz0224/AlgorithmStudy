def solution(msg):
    index = 0
    dic = dict()
    arr = []
    for i in range(65,91):
        dic[chr(i)] = i-64
    index = 27
    i = 0
    s = ""
    while i < len(msg):
        s += msg[i]
        if s in dic.keys():
            i += 1
        else:
            dic[s] = index
            index += 1
            arr.append(dic[s[:-1]])
            s = ""
    arr.append(dic[s])
    return arr