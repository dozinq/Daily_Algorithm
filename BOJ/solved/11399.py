import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

data = sorted(list(map(int, input().split())))

ans = 0
# tmp = 0
# for i in data:
#     tmp += i
#     ans += tmp

# 1+ 1+2+ 1+2+3+ 1+2+3+3+ 1+2+3+4
# 1은 N만큼, 2는 N-1만큼, ... i는 1만큼 더한다.
cnt = 1
for i in range(N-1, -1, -1):
    ans += data[i] * cnt
    cnt += 1

print(ans)

