import sys
sys.stdin = open('BOJ/input.txt')

N, M, P = map(int, input().split())
cnt = 1
same_cnt = 0
if N > 0:
    data = list(map(int, input().split()))

for i in range(N):
    if data[i] > M:
        cnt += 1
    if data[i] == M:
        same_cnt += 1

if cnt + same_cnt > P:
    cnt = -1
print(cnt)