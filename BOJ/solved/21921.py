import sys
sys.stdin = open('BOJ/input.txt')

N, X = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))

start = 0
end = X - 1
cnt = sum(data[start:end+1])
ans = [cnt, 1]
while end < N-1:
    end += 1
    cnt += data[end] - data[start]
    if cnt == ans[0]:
        ans[1] += 1
    elif cnt > ans[0]:
        ans[0], ans[1] = cnt, 1
    start += 1

if ans[0] == 0:
    print('SAD')
else:
    print(ans[0])
    print(ans[1])