import sys
sys.stdin = open('BOJ/input.txt')

H, W, N, M = map(int, input().split())
ans = 0
if H % (N + 1) != 0:
    ans = (H // (N + 1)) + 1
else:
    ans = (H // (N + 1))

if W % (M + 1) != 0:
    ans *= (W // (M + 1)) + 1
else:
    ans *= (W // (M + 1))

print(ans)