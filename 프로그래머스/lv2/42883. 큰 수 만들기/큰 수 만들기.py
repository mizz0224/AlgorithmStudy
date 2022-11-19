
def solution(number, k):
    arr = []
    for num in number:
        while len(arr) > 0 and arr[-1] < num and k > 0 :
            k -= 1
            arr.pop()
        arr.append(num)
    return "".join(arr[:len(arr)-k])