from itertools import permutations


def solution(expression):
    #symbolSet = set()
    answers = []
    #for ch in expression:
    #    if ch in ["+", "-", "*"]:
    #        symbolSet.add(ch)
    #orders = list(permutations(symbolSet, len(symbols)))
    orders = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    for order in orders:
        answers.append(cal(expression, order))
    
    return max(answers)


def cal(expression, order):
    temp_list = []
    for e in expression.split(order[0]):
        temp = [f"({i})" for i in e.split(order[1])]
        temp_list.append(f'({order[1].join(temp)})')

    return abs(eval(order[0].join(temp_list)))