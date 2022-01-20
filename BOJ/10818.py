import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

min_lst = lst[0]
max_lst = lst[0]

for i in range(N):
    if lst[i] < min_lst:
        min_lst = lst[i]
    if lst[i] > max_lst:
        max_lst = lst[i]

print('%d %d' % (min_lst, max_lst))