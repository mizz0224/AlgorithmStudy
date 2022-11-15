def solution(want, number, discount):
    answer = 0
    dic = dict()
    for i in range(0,len(want)):
        dic[want[i]] = number[i]
    for i in range(0,len(discount)):
        tmp = dic.copy()
        for j in range(i,len(discount) if i+10 > len(discount) else i+10):
            item = discount[j]
            if item in tmp.keys() :
                if tmp[item] > 0 :
                    tmp[item] -= 1
        values = list(tmp.values())
        if values.count(0) == len(values) :
            answer += 1
    return answer