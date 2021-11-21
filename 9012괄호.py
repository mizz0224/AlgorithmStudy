import sys

result_arr = list()
count_num = int(sys.stdin.readline())
for _ in range(count_num):
    line = sys.stdin.readline().rstrip()
    barcket_count = 0
    result = "YES"
    for barcket in line:
        if barcket == "(":
            barcket_count += 1
        else:
            barcket_count -= 1
        if barcket_count < 0:
            result = "NO"
            break
    if barcket_count != 0:
        result = "NO"
    result_arr.append(result)

for result in result_arr:
    print(result)
