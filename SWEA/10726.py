import sys
sys.stdin = open('input.txt')

def check_ans(num):
    if len(num) < N:
        return 0
    for i in range(len(num)-N, len(num)):
        if ans[i] == '0':
            return 0
    return 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = format(M, 'b')

    # if len(ans) < N:
    #     N = len(ans)

    if check_ans(ans) == 1:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')



