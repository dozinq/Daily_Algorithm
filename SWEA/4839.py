def BinSearch(l, r):
    return int((l+r)/2)

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    ans_lst = []
    for page in (Pa, Pb):
        left = 1
        right = P
        num = 0
        while (1):
            num += 1
            tmp = BinSearch(left, right)
            if page < tmp:
                right = tmp
            elif page > tmp:
                left = tmp
            if page == tmp:
                ans_lst.append(num)
                break

    if ans_lst[0] < ans_lst[1]:
        ans = 'A'
    elif ans_lst[0] > ans_lst[1]:
        ans = 'B'
    else:
        ans = 0

    print(f'#{tc} {ans}')