import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()
response_arr = list()
for _ in range(n):
    message = sys.stdin.readline().rstrip()
    response = ""
    if message[-1].isdigit():
        command, num = message.split()
        arr.append(num)
    else:
        if message == "pop":
            try:
                element = arr.pop()
                response = str(element)
            except:
                response = "-1"
        elif message == "size":
            try:
                element = len(arr)
                response = str(element)
            except:
                response = str(-1)
        elif message == "empty":
            element = len(arr)
            if element == 0:
                response = "1"
            else:
                response = str(0)
        elif message == "top":
            try:
                element = arr[-1]
                if element == None:
                    response = "-1"
                else:
                    response = str(element)
            except:
                response = str(-1)
        response_arr.append(response)


for i in response_arr:
    print(i)
