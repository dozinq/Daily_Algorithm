import sys
sys.stdin = open('input.txt')

def find_three(where, cnt):                 # 스택을 배워도 써먹질 못했던 코드이다.. 그래도 풀리긴 하는데 다음부턴 응용해보자고!
    if where not in visited:                # 방문하지 않았다면,
        visited.append(where)               # 방문처리하고~~
        for n in range(4):                  # 방향 델타를 반복시켜서 길을 찾자~~!
            if 0 <= where[0] + dr[n] < N and 0 <= where[1] + dc[n] < N:
                if data[where[0] + dr[n]][where[1] + dc[n]] == 3:
                    ans_lst.append(cnt)
                if data[where[0] + dr[n]][where[1] + dc[n]] == 0:
                    find_three((where[0] + dr[n], where[1] + dc[n]), cnt+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [[0]*N for _ in range(N)]

    for i in range(N):                      # data를 저장할 때 번거롭게 저장할 수 있었다..
        tmp = int(input())                  # 되긴 되더라.. 근데 고칠 필요가 있다..!
        for j in range(N-1, -1, -1):
            data[i][j] = tmp % 10
            tmp //= 10
    dr = [0, 1, 0, -1]                      # 방향벡터의 저장.. 이 또한 튜플형식으로 한줄로 만들 수 있다!
    dc = [1, 0, -1, 0]

    for i in range(len(data)):              # 시작지점을 찾는다! (도착지점부터 찾을걸)
        for j in range((len(data))):
            if data[i][j] == 2:
                start = i, j
                break                       # 반복문에서 더 빨리 break 시킬 수 있더라(병승이 코드 참고!)

    visited = []
    ans_lst = []
    find_three(start, 0)                    # 거리를 0으로 설정하고 시작지점부터 실행!
    if len(ans_lst) == 0:                   # 도착지점을 못 찾았다면 임의로 0을 저장한다.
        ans_lst.append(0)
    print(f'#{tc} {min(ans_lst)}')          # 거리 중에 최솟값을 출력한다.