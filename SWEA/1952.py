T = int(input())

for tc in range(1, T+1):
    daily, month, three_month, year = map(int, input().split())
    data = list(map(int, input(). split()))         # 0 ~ 11
    ans_lst = [0]*13                                # 0 ~ 12
    ans_lst[1] = min(daily*data[0], month)
    ans_lst[2] = ans_lst[1] + min(daily*data[1], month)
    for n in range(3, 13):
        ans_lst[n] = ans_lst[n-1] + min(daily*data[n-1], month)
        ans_lst[n] = ans_lst[n-3] + min(ans_lst[n]-ans_lst[n-3], three_month)

    print(f'#{tc} {min(ans_lst[12], year)}')