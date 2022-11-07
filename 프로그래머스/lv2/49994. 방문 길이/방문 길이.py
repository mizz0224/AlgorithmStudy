def solution(dirs):
    rooted = []
    nowLoc = [0,0]
    overlapCount = 0
    count = 0
    for dir in dirs:
        nowLocX = nowLoc[0]
        nowLocY = nowLoc[1]
        if dir == "U":
            nowLocY += 1
        elif dir == "D":
            nowLocY -= 1
        elif dir == "L":
            nowLocX -= 1
        elif dir == "R":
            nowLocX += 1
        #print([nowLocX,nowLocY])
        if nowLocX in range(-5,6) and nowLocY in range(-5,6):
            new = [nowLocX,nowLocY]
            root = [nowLoc,new]
            root2 = [new,nowLoc]
            nowLoc = new
            if root in rooted or root2 in rooted :
                pass
            else :
                rooted.append(root)
                rooted.append(root2)
                count += 1
    return count