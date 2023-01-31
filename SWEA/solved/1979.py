import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    num_lst_col = []
    for i in range(len(num_lst)):
        tmp_str = []
        for j in range(len(num_lst)):
            tmp_str.append(num_lst[j][i])
        num_lst_col.append(tmp_str)

    key = [1]*K
    ans = 0
    for i in range(N):
        for j in range(0, N-K+1):
            if num_lst[i][j:j+K] == key:
                if j+K == N:                # 오른쪽 인덱스일 경우,
                    if num_lst[i][j-1] == 0:
                        ans += 1
                elif j == 0:                # 왼쪽 인덱스일 경우,
                    if num_lst[i][j+K] == 0:
                        ans += 1
                else:                       # 그 외, 왼쪽오른쪽 인덱스 비교
                    if num_lst[i][j-1] == 0 and num_lst[i][j+K] ==0:
                        ans += 1
            if num_lst_col[i][j:j+K] == key:
                if j+K == N:
                    if num_lst_col[i][j-1] == 0:
                        ans += 1
                elif j == 0:
                    if num_lst_col[i][j+K] == 0:
                        ans+=1
                else:
                    if num_lst_col[i][j-1] == 0 and num_lst_col[i][j+K] ==0:
                        ans+=1
    print(f'#{tc} {ans}')