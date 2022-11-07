def solution(files):
    answer = []
    arr = []
    for file in files:
        numberFounded = False
        numberStartIndex = 0
        numberEndIndex = len(file)
        for index in range(0,len(file)):
            if file[index].isdigit() and numberFounded == False:
                numberStartIndex = index
                numberFounded = True
            if file[index].isdigit() == False and numberFounded == True:
                numberEndIndex = index
                break
        print(numberEndIndex)
        head = file[0:numberStartIndex]
        number = file[numberStartIndex:numberEndIndex]
        tail = file[numberEndIndex:]
        arr.append([head,number,tail])
    arr.sort(key=lambda x: (x[0].lower(),int(x[1])))
    
    for file in arr:
        head = file[0]
        number = file[1]
        tail = file[2]
        answer.append(head+number+tail)
    return answer