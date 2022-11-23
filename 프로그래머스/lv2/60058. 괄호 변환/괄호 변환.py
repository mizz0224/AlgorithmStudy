def solution(p):
    #1.
    if p == "" :
        return ""
    #2.
    u,v = spliter(p)
    #3.
    if check(u):
        #3-1.
        return u + solution(v)
    #4.
    else:
        #4-1.
        answer = "("
        #4-2.
        answer += solution(v)
        #4-3.
        answer += ")"
        #4-4.
        for p in u[1:-1]:
            if p == "(":
                answer += ")"
            else:
                answer += "("
        return answer
def spliter(w):
    openCounter = 0
    closeCounter = 0
    u = ""
    v = ""
    for i in range(0,len(w)):
        if w[i] == "(":
            openCounter += 1
        else :
            closeCounter += 1
        if openCounter == closeCounter :
            u = w[:i+1]
            v = w[i+1:]
            break
    return u,v 

def check(w):
    howOpen = 0
    for i in range(0,len(w)):
        if w[i] == "(":
            howOpen += 1
        else :
            howOpen -= 1
        if howOpen < 0:
            return False
    return howOpen == 0