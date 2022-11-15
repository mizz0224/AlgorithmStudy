from itertools import permutations
def solution(numbers):
    permutationArr = []
    answer = 0
    
    for i in range(1,len(numbers)+1):
        permutationArr+=list(map(''.join, permutations(numbers, i)))
    
    permutationArr = list(set([int(i) for i in permutationArr]))
    permutationArr.sort()
    biggest = permutationArr[-1] + 1
    isPrime = [True] * biggest
    m = int(biggest ** 0.5)
    
    for i in range(2,m+1) :
        if isPrime[i] == True :
            for j in range(i*2, biggest, i):
                isPrime[j] = False

    for number in permutationArr:
        if isPrime[number] == True and number > 1:
            answer += 1
    return answer