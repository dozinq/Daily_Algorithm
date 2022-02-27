import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    _, lst = map(list, input().split())     # N은 사용하지 않으므로 받기만 하였다.
    ans_lst = []
    index = 0
    for index in range(0, len(lst)):
        if len(ans_lst) == 0:               # ans_lst에 아무것도 담겨있지 않다면, lst의 index값을 추가한다.
            ans_lst.append(lst[index])
        elif ans_lst[-1] == lst[index]:     # ans_lst에서 가장 최근에 담겨진 원소랑 lst의 index값이 일치하다면 ans_lst에서 제거한다.
            ans_lst.pop()
        else:
            ans_lst.append(lst[index])      # ~와 다르다면 추가한다.

    print(f'#{tc} {"".join(ans_lst)}')