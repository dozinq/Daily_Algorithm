import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())

# 첫번째 조건
if sum(data) <= M:
    print(data[-1])
else:
    # 두번째 조건
    ans = 0
    start = 0
    end = data[-1]
    while start <= end:
        tmp = 0
        mid = (start + end) // 2
        for i in range(len(data)):
            if data[i] < mid:
                tmp += data[i]
            elif data[i] >= mid:
                tmp += mid
        if tmp <= M:
            start = mid + 1
        elif tmp > M:
            end = mid - 1
    ans = end
    print(ans)