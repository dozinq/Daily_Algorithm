import sys
sys.stdin = open('BOJ/input.txt')

N, M = input().split()
N = int(N)
if M == 'Y':
    limit = 1
elif M == 'F':
    limit = 2
else:
    limit = 3

ans = 0
cnt = 0
data = set()
for _ in range(N):
    tmp = sys.stdin.readline().strip()
    data.add(tmp)
ans = len(data) // limit
print(ans)