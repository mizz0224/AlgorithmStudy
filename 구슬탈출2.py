import sys

sys.setrecursionlimit(10 ** 7)


column, row = map(int, input().split())

# array = [["#" for col in range(column)] for row in range(row)]

#
#  for i in range(column):
#     for j in range(row):
#         array[i][j] =
array = list()
for i in range(column):
    array.append(list(input()))


def findchar(target):
    for i in range(column):
        for j in range(row):
            if array[i][j] == target:
                return i, j


red_y, red_x = findchar("R")


def finddirect(red_y, red_x, direction, count):

    if array[red_y][red_x] == "O":
        return count

    if red_y == 0:
        north = "#"
    else:
        north_y = red_y - 1
        north_x = red_x
        north = array[north_y][north_x]

    if red_y == column:
        south = "#"
    else:
        south_y = red_y + 1
        south_x = red_x
        south = array[south_y][south_x]

    if red_x == 0:
        west = "#"
    else:
        west_y = red_y
        west_x = red_x - 1
        west = array[west_y][west_x]

    if red_x == column:
        east = "#"
    else:
        east_y = red_y
        east_x = red_x + 1
        west = array[east_y][east_x]

    if north == ".":
        if direction != "north":
            count += 1
            direction = "north"
        finddirect(north_y, north_x, direction, count)
    else:
        pass

    if south == ".":
        if direction != "south":
            count += 1
            direction = "south"
        finddirect(south_y, south_x, direction, count)
    else:
        pass

    if west == ".":
        if direction != "west":
            count += 1
            direction = "west"
        finddirect(west_y, west_x, direction, count)
    else:
        pass

    if east == ".":
        if direction != "east":
            count += 1
            direction = "east"
        finddirect(east_y, east_x, direction, count)
    else:
        pass


print(finddirect(red_y, red_x, "none", 0))
