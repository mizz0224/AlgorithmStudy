import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()
response_arr = list()
for _ in range(n):
    message = sys.stdin.readline().strip()
    response = ""
    if message[-1].isdigit():
        command, num = message.split()
        num = int(num)
        if command == "push_front":
            arr.appendleft(num)
        elif command == "push_back":
            arr.append(num)
        else:
            response = "error_1"
            response_arr.append(response)
    else:
        if message == "pop_front":
            try:
                element = arr.popleft()
                response = str(element)
            except:
                response = "-1"

        elif message == "pop_back":
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
        elif message == "front":
            try:
                element = arr[0]
                if element == None:
                    response = "-1"
                else:
                    response = str(element)
            except:
                response = str(-1)
        elif message == "back":
            try:
                element = arr[-1]
                if element == None:
                    response = "-1"
                else:
                    response = str(element)
            except:
                response = str(-1)
        else:
            response = "error_2"
        response_arr.append(response)


for i in response_arr:
    print(i)
