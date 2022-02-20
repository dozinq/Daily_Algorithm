T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    my_lst = [0]*N
    i = 0
    for _ in range(Q):
        i += 1
        L, R = map(int, input().split())
        for index in range(L-1, R):
            my_lst[index] = i
    print(f'#{tc} ', end='')
    print(*my_lst)