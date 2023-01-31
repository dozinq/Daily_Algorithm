import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ABC_lst = [list(input())for _ in range(8)]
    ABC_lst_col = list(map(list, zip(*ABC_lst)))
    test_lst = []
    ans = 0

    for i in range(8):
        for j in range(8):
            if j+N-1 < 8:
                test_lst.append(ABC_lst[i][j:j+N])
                test_lst.append(ABC_lst_col[i][j:j+N])

    for index in test_lst:
        cnt = 0
        for a in range(N//2):
            if index[a] != index[-1*(a+1)]:
                break
            else:
                cnt += 1
        if cnt == N//2:
            ans +=1

    print(f'#{tc} {ans}')