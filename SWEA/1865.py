import sys
sys.stdin = open('input.txt')

def work(num, dist):
    global ans
    if dist <= ans:                 # 이 부분을 가지치기로 추가해주었는데, 사실 이해가 잘 안간다.. 리뷰시간에 꼭 물어봐야 겠다!
        return
    if num == N:
        ans = max(dist, ans)
    for i in range(N):
        if not visited[i] and data[num][i] != 0:
            visited[i] = 1
            work(num+1, dist*data[num][i]/100)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 0
    work(0, 1)
    print(f'#{tc} {ans*100:.6f}')