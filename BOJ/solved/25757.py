"""
set()을 사용하지 않았고, in을 사용하여 연산할 수 있게 하여 시간 초과 발생.
-> 25757-1.py 라는 이름의 파일로 수정.
"""

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
data = []
for _ in range(N):
    tmp = sys.stdin.readline().strip()
    if tmp not in data:
        data.append(tmp)
        cnt += 1
        if limit == cnt:
            ans += 1
            cnt = 0
print(ans)