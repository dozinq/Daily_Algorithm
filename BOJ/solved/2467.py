import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = [i for i in map(int, input().split())]

ans = [0, 0, float('INF')]

for idx in range(N - 1):
    start = idx + 1
    end = N-1
    while start <= end:
        mid = (start + end) // 2

        if abs(data[mid] + data[idx]) < ans[2]:
            ans = [data[idx], data[mid], abs(data[mid] + data[idx])]

        if data[mid] + data[idx] < 0:
            start = mid + 1
        else:
            end = mid - 1

print(f'{ans[0]} {ans[1]}')