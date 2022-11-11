def solution(elements):
    resultSet = set()
    elementsLen = len(elements)
    elements *= 2
    for i in range(1,elementsLen+1):
        for j in range(0,elementsLen):
                resultSet.add(sum(elements[j:j+i]))
    return len(resultSet)