import sys
sys.stdin = open('BOJ/input.txt')

N, K = map(int, input().split())
data = list(sys.stdin.readline())
visited = [0 for _ in range(len(data))]

cnt = 0
for i in range(len(data)):
    if data[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N:
                if data[j] == 'H' and visited[j] == 0:
                    cnt += 1
                    visited[j] = 1
                    break
print(cnt)