for tc in range(1, 11):
    L = int(input())
    lst = list((input()))
    stack = []
    ans = []
    dic = {'+': 1, '*': 2}
    for index in lst:
        if index in '+*':
            while stack and dic[index] <= dic[stack[-1]]:
                ans.append(stack.pop())
            stack.append(index)
        else:
            ans.append(index)
    while stack:
        ans.append(stack.pop())
    answer = ''.join(ans)

    for index in answer:
        if index in '+':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a+b)
        elif index in '*':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a*b)
        else:
            stack.append(index)
    print(f'#{tc} {stack[0]}')