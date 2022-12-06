def solution(rows, columns, queries):
    answer = []
    answerArr = []
    number = 1
    for i in range(0,rows):
        tmp = []
        for j in range(0,columns):
            tmp.append(number)
            number+=1
        answer.append(tmp)
    for query in queries:
        startR,startC,endR,endC = query
        startR -= 1
        startC -= 1
        endR -= 1
        endC -= 1
        nowR = startR
        nowC = startC+1
        lastNum = answer[startR+1][startC]
        tmp = answer[startR][startC]
        queryArr = []
        queryArr.append(tmp)
        while True:
            #맨 윗줄
            if nowR == startR :
                #맨 윗줄, 맨 왼쪽 : 종료
                if nowC == startC:
                    break
                #맨 윗줄, 맨 오른쪽
                if nowC == endC :
                    nextR = nowR +1
                    nextC = nowC
                #맨 윗줄이며 맨 오른쪽이 아닐때
                else:
                    nextR = nowR 
                    nextC = nowC +1
            #맨 아랫줄
            elif nowR == endR :
                #맨 아랫줄, 맨 왼쪽일때
                if nowC == startC :
                    nextR = nowR -1
                    nextC = nowC 
                #맨 아랫줄, 맨 왼쪽이 아닐때
                else:
                    nextR = nowR 
                    nextC = nowC -1
            #좌측 기둥 
            elif nowC == startC :
                #좌측 기둥이며 맨 윗줄 일때
                if nowR == startR :
                    break
                #좌측 기둥이며 맨 윗줄이 아닐때
                else :
                    nextR = nowR -1
                    nextC = nowC 

            #우측 기둥
            elif nowC == endC :
                #우측 기둥이며 맨 아랫줄일때
                if nowR == endR :
                    nextR = nowR 
                    nextC = nowC -1
                #우측 기둥이며 맨 아랫줄이 아닐때
                else :
                    nextR = nowR +1
                    nextC = nowC 

            #에러났을때
            else :
                print("error")
                print(nowR,nowC)
                print(nextR,nextC)
                return answer

            
            old = answer[nowR][nowC]
            answer[nowR][nowC] = tmp
            tmp = old
            nowR = nextR
            nowC = nextC
            queryArr.append(tmp)
        answer[startR][startC] = lastNum
        queryArr.append(lastNum)
        answerArr.append(min(queryArr))
        # for i in answer:
        #     print(i)
        # kkk = input()
    return answerArr