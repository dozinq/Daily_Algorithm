import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1])   # 종료 시간을 기준으로 정렬시킨다.
    ans = 1
    now = data[0][1]
    for i in range(1, N):
        if data[i][0] >= now:
            ans += 1
            now = data[i][1]
    print(f'#{tc} {ans}')