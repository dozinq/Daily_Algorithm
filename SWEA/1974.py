import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num_lst = [list(map(int, input().split())) for _ in range(9)]
    num_lst_col = list(zip(*num_lst))

    ans = 1

    col = 0
    for _ in range(3):                  # 3*3의 작은 상자들이 올바른지 검사하는 반복문
        i = 0
        tmp_num = 0
        for _ in range(9):
            tmp_num += sum(num_lst[i][col:col+3])
            i += 1
            if i % 3 == 0:
                if tmp_num == 45:
                    tmp_num = 0
                else:
                    ans = 0
        col += 3

    sort_lst = [num for num in range(1, 10)]

    for i in range(9):                  # 가로, 세로가 올바른지 검사하는 반복문
        if sorted(num_lst[i]) != sort_lst:
            ans = 0
        if sorted(num_lst_col[i]) != sort_lst:
            ans = 0

    print(f'#{tc} {ans}')