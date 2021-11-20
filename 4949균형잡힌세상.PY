import sys

result_arr = list()
while True:
    line = sys.stdin.readline()
    sentence, dot = line.split(".")
    # result_arr.append(sentence)
    if sentence == "":
        break
    result = "yes"
    barcket_count = {"(": 0, "[": 0}
    barcket_arr = list()
    for letter in sentence:

        if letter in barcket_count.keys():
            barcket_count[letter] += 1
            barcket_arr.append(letter)
        if len(barcket_arr) != 0:
            if barcket_arr[-1] == "(" and letter == "]":
                result = "no"
                break
            elif barcket_arr[-1] == "[" and letter == ")":
                result = "no"
                break
        if letter == ")":
            barcket_count["("] -= 1
            if len(barcket_arr) != 0:
                barcket_arr.pop()
            if barcket_count["("] < 0:
                result = "no"
                break
        if letter == "]":
            barcket_count["["] -= 1
            if len(barcket_arr) != 0:
                barcket_arr.pop()
            if barcket_count["["] < 0:
                result = "no"
                break

    for barcket in barcket_count.keys():
        if barcket_count[barcket] != 0:
            result = "no"
    result_arr.append(result)
# print("////////////////////////////////")
for result in result_arr:
    print(result)
