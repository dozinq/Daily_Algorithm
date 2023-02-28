import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
cnt = [0 for _ in range(N+1)]
ans = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        cnt[i] = 0
        ans[i] = 0
    else:
        cnt[i] = cnt[i-1] + 1
        ans[i] = i - 1

        if i % 3 == 0 and cnt[i] > cnt[i//3] + 1:
            cnt[i] = cnt[i//3] + 1
            ans[i] = i//3

        if i % 2 == 0 and cnt[i] > cnt[i//2] + 1:
            cnt[i] = cnt[i//2] + 1
            ans[i] = i//2

print(cnt[N])

while N > 0:
    print(N, end = ' ')
    N = ans[N]