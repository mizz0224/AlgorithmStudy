from itertools import combinations
def solution(orders, course):
    combinationsArr = []
    dic = dict()
    answerDic = dict()
    answer = []
    for order in orders:
        for i in course:
            combinationsArr=combinations(order,i)
            for combination in combinationsArr:
                sortedCombination = list(combination)
                sortedCombination.sort()
                sortedCombination = "".join(sortedCombination)
                if sortedCombination in dic.keys():
                    dic[sortedCombination] += 1
                else :
                    dic[sortedCombination] = 1
    
    for key in dic.keys():
        keyLen = len(key)
        if keyLen in answerDic.keys():
            if answerDic[keyLen] < dic[key]:
                answerDic[keyLen] = dic[key]
        else:
            answerDic[keyLen] = dic[key]
    
    for key in dic.keys():
        keyLen = len(key)
        count = answerDic[keyLen]
        if count == dic[key] and count>1:
            answer.append(key)
    answer.sort()    
    return answer