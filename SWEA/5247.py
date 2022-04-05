import sys
sys.stdin = open('input.txt')
from collections import deque

def cal(n):
    global ans
    cnt = 0
    deq = deque([n])
    num_lst = [0] * 1000001
    tmp_lst = deque()

    while not ans:
        while deq:
            num = deq.popleft()
            if num == M:
                ans = cnt
                return
            a, b, c, d = num + 1, num * 2, num - 1, num - 10
            if 0 <= a <= 1000000 and not num_lst[a]:
                tmp_lst.append(a)
                num_lst[a] = True
            if 0 <= b <= 1000000 and not num_lst[b]:
                tmp_lst.append(b)
                num_lst[b] = True
            if 0 <= c <= 1000000 and not num_lst[c]:
                tmp_lst.append(c)
                num_lst[c] = True
            if 0 <= d <= 1000000 and not num_lst[d]:
                tmp_lst.append(d)
                num_lst[d] = True
        cnt += 1
        deq, tmp_lst = tmp_lst, deq

    return

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    cal(N)

    print(f'#{tc} {ans}')
