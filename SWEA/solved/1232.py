import sys
sys.stdin = open('input.txt')

def find_ans(node):
    if data[node][0] >= 0:
        return data[node][0]
    else:
        if data[node][0] == -1:                                         # '+'일때,
            return find_ans(data[node][1]) + find_ans(data[node][2])
        elif data[node][0] == -2:                                       # '-'일때,
            return find_ans(data[node][1]) - find_ans(data[node][2])
        elif data[node][0] == -3:                                       # '*'일때,
            return find_ans(data[node][1]) * find_ans(data[node][2])
        elif data[node][0] == -4:                                       # '/'일때,
            return find_ans(data[node][1]) / find_ans(data[node][2])

for tc in range(1, 11):
    N = int(input())
    data = [[0]*3 for _ in range(N+1)]
    for i in range(1, N+1):
        tmp = input().split()

        if len(tmp) == 4:
            if tmp[1] == '+':                                           # '+'일때,
                data[i][0] = -1
            elif tmp[1] == '-':                                         # '-'일때,
                data[i][0] = -2
            elif tmp[1] == '*':                                         # '*'일때,
                data[i][0] = -3
            elif tmp[1] == '/':                                         # '/'일때,
                data[i][0] = -4
            data[i][1], data[i][2] = int(tmp[2]), int(tmp[3])
        else:
            data[i][0] = int(tmp[1])
    ans = int(find_ans(1))
    print(f'#{tc} {ans}')
