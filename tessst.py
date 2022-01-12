end = 1
start = -1
while end < 100000:
    for a in range(start, end):
        for b in range(start, end):
            for c in range(start, end):
                for d in range(start, end):
                    for e in range(start, end):
                        if 5 * e + 40 * d + 300 * c + 2000 * d + 10000 * a == (
                            e + 10 * d + 100 * c + 1000 * b + 10000 * a
                        ):
                            if a + b + c + d + e == 30:
                                print(a, b, c, d, e)
    print(start, "부터", end, "까지에서 찾기 실패하였습니다.")
    end *= 10
    start *= 10
# a = 2
# b = 13
# c = 4
# d = 6
# e = 5
# if (
#     a * 10000 + b * 2000 + c * 300 + d * 40 + e * 5
#     == a * 10000 + b * 1000 + c * 100 + d * 10 + e
# ):
#     print("맞음")
# else:
#     print("틀림")
