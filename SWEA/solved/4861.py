import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_lst = [list(input()) for _ in range(N)]
    word_lst_col = list(map(list, zip(*word_lst)))
    test_lst = []
    ans_lst = []

    for i in range(N):
        for j in range(N):
            if j+M-1 < N:
                test_lst.append(word_lst[i][j:j+M])
                test_lst.append(word_lst_col[i][j:j+M])

    for index in test_lst:
        cnt = 0
        for num in range(M):
            if index[num] != index[-1*(num+1)]:
                break
            cnt += 1
            if cnt == M//2:
                ans_lst = index
    print(f'#{tc}', end=' ')
    for i in ans_lst:
        print(i, end='')
    print()