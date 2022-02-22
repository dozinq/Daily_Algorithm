T = int(input())

for tc in range(1, T+1):
    my_str = input()
    tmp_lst = []
    ans = 1
    for index in my_str:
        if index == '(':
            tmp_lst.append('(')
        elif index == '{':
            tmp_lst.append('{')
        elif index == ')':
            if tmp_lst.count('(') == 0:
                ans = 0
                break
            if tmp_lst[-1] == '(':
                tmp_lst.pop()
            else:
                ans = 0
                break
        elif index == '}':
            if tmp_lst.count('{') == 0:
                ans = 0
                break
            if tmp_lst[-1] == '{':
                tmp_lst.pop()
            else:
                ans = 0
                break
        else:
            continue
    if len(tmp_lst) != 0:
        ans = 0
    print(f'#{tc} {ans}')