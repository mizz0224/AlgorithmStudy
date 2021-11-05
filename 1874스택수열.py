n = int(input())
stack = list()
result = list()
count = 0
fail = False
for i in range(1, n + 1):
    stack_num = int(input())
    while count < stack_num:
        count += 1
        result.append("+")
        stack.append(count)
    if stack[-1] == stack_num:
        stack.pop()
        result.append("-")
    else:
        fail = True

if fail:
    print("NO")
else:
    print("\n".join(result))
