import sys
sys.stdin = open('input.txt')

def in_order(node):
    if node:
        in_order(data[node][2])
        print(data[node][1], end='')
        in_order(data[node][3])

for tc in range(1, 11):
    N = int(input())
    data = [[0]*4 for _ in range(N+1)]
    for i in range(1, N+1):
        tmp_lst = input().split()
        for index in range(len(tmp_lst)):
            if index == 1:
                data[i][index] = tmp_lst[index]
            else:
                data[i][index] = int(tmp_lst[index])

    print(f'#{tc}', end=' ')
    in_order(1)
    print()