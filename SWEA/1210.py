import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    ladder_lst = [list(map(int, input().split())) for _ in range(100)]

    for index in range(100):
        if ladder_lst[99][index] == 2:
            col = index
    row = 99
    flag = 2
    while (row > 0):
        if col+1 < 100 and ladder_lst[row][col+1] == 1 and flag != 0:
            col += 1
            flag = 1
        elif col-1 >0 and ladder_lst[row][col-1] == 1 and flag != 1:
            col -= 1
            flag = 0
        else:
            row -= 1
            flag = 2

    print(f'#{tc} {col}')