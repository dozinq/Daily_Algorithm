import sys
sys.stdin = open('BOJ/input.txt')

def find(x):
    start = 0
    end = cnt
    while start <= end:
        mid = (start + end) // 2
        if memo[mid] >= x:
            end = mid - 1
        elif memo[mid] < x:
            start = mid + 1
    return mid

N = int(input())
data = list(map(int, sys.stdin.readline().split()))

memo = [float('inf') for _ in range(N+1)]
memo[0] = data[0]

cnt = 0
for i in range(1, len(data)):
    if memo[cnt] < data[i]:
        cnt += 1
        memo[cnt] = data[i]
        continue
    if memo[cnt] > data[i]:
        target = find(data[i])
        # 탐색하여 일치하는 값을 못 찾았을 경우를 대비한다.
        if memo[target] < data[i]:
            memo[target+1] = data[i]
        elif memo[target] > data[i]:
            memo[target] = data[i]

ans = cnt+1
print(ans)