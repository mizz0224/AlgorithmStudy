def solution(n, t, m, p):
    totalNum = ''
    answer = ''
    for i in range(0,t*m):
        totalNum += converter(i,n)
    for i in range(0,t):
        answer += totalNum[p-1+m*i]
    return answer
def converter(t,n):
    num = "0123456789ABCDEF"
    quo, rem = divmod(t,n)
    return converter(quo,n) + num[rem] if quo else num[rem]