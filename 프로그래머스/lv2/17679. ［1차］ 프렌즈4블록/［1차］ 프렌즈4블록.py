def solution(m, n, board):
    board2 = []
    count = 0
    for i in board:
        tmp = []
        for j in i:
            tmp.append(j)
        board2.append(tmp)
    while True:
        toErase = []
        for i in range(0,m):
            for j in range(0,n):
                if board2[i][j] == "o" :
                    continue
                if i > 0 and j > 0 :
                    leftUp = [i-1,j-1]
                    rightUp = [i-1,j]
                    leftDown = [i,j-1]
                    rightDown = [i,j]
                    if board2[leftUp[0]][leftUp[1]] == board2[rightUp[0]][rightUp[1]] == board2[leftDown[0]][leftDown[1]] ==board2[rightDown[0]][rightDown[1]] :
                        toErase.append(leftUp)
                        toErase.append(rightUp)
                        toErase.append(leftDown)
                        toErase.append(rightDown)
                if i > 0 and j < n-1 :
                    leftUp = [i-1,j]
                    rightUp = [i-1,j+1]
                    leftDown = [i,j]
                    rightDown = [i,j+1]
                    if board2[leftUp[0]][leftUp[1]] == board2[rightUp[0]][rightUp[1]] == board2[leftDown[0]][leftDown[1]] ==board2[rightDown[0]][rightDown[1]] :
                        toErase.append(leftUp)
                        toErase.append(rightUp)
                        toErase.append(leftDown)
                        toErase.append(rightDown)
                if i < m-1 and j < n-1 :
                    leftUp = [i,j]
                    rightUp = [i,j+1]
                    leftDown = [i+1,j]
                    rightDown = [i+1,j+1]
                    if board2[leftUp[0]][leftUp[1]] == board2[rightUp[0]][rightUp[1]] == board2[leftDown[0]][leftDown[1]] ==board2[rightDown[0]][rightDown[1]] :
                        toErase.append(leftUp)
                        toErase.append(rightUp)
                        toErase.append(leftDown)
                        toErase.append(rightDown)
                if i < m-1 and j > 0 :
                    leftUp = [i,j-1]
                    rightUp = [i,j]
                    leftDown = [i+1,j-1]
                    rightDown = [i+1,j]
                    if board2[leftUp[0]][leftUp[1]] == board2[rightUp[0]][rightUp[1]] == board2[leftDown[0]][leftDown[1]] ==board2[rightDown[0]][rightDown[1]] :
                        toErase.append(leftUp)
                        toErase.append(rightUp)
                        toErase.append(leftDown)
                        toErase.append(rightDown)
        if len(toErase) == 0 :
            break       
        else :
            for i in toErase :
                if not board2[i[0]][i[1]] == "o" :
                    board2[i[0]][i[1]] = "o"
                    count += 1
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if board2[i][j] == "o" :
                        check = False
                        toDown = 0
                        for k in range(i,-1,-1) :
                            if not board2[k][j] == "o" :
                                check = True
                                toDown = k
                                break
                        if check : 
                            board2[i][j] = board2[toDown][j]
                            board2[toDown][j] = "o"
        toErase.clear()
    return count