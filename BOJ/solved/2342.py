import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit(10**6)

def dance(pos, next):
    if pos == next:
        return 1
    if pos == 0:
        return 2
    if (pos + next) % 2 == 1:
        return 3
    if (pos + next) % 2 == 0:
        return 4

def DDR(n, l, r):
    if data[n] == 0:
        return 0
    if ans_lst[n][l][r] != -1:
        return ans_lst[n][l][r]
    ans_lst[n][l][r] = min(DDR(n+1, data[n], r) + dance(l, data[n]), DDR(n+1, l, data[n]) + dance(r, data[n]))
    return ans_lst[n][l][r]

data = list(map(int, sys.stdin.readline().split()))

ans_lst = [list(list(-1 for _ in range(5)) for _ in range(5)) for _ in range(len(data))]

print(DDR(0, 0, 0))
