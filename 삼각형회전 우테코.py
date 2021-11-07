def solution(grid, clockwise):
    old = []
    answer = []
    width = 0
    heigh = 0
    for gr in grid:
        line = list()
        line_count = 0
        for g in gr:
            line.append(g)
            line_count += 1
        if line_count > width:
            width = line_count
        old.append(line)
        heigh += 1
    for i in range(heigh):
        line = list()
        for j in range(width):
            list.append(old[])
    return answer


print(solution(["1", "234", "56789"], True))
