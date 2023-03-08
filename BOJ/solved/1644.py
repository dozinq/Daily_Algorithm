import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

# 1. 시간 최적화를 위해, 에라토스테네스의 체 구현
data = [1] * (N+1)
data[0], data[1] = 0, 0
for i in range(2, N+1):
    if data[i] == 1:
        for j in range(2, (N//i)+1):
            data[i*j] = 0

lst = []
for i in range(len(data)):
    if data[i] == 1:
        lst.append(i)

# 2. 투포인터 알고리즘을 사용하여 탐색
start = 0
end = 1
ans = 0
while end <= len(lst):
    tmp = sum(lst[start:end])
    if tmp > N:
        start += 1
    elif tmp < N:
        end += 1
    elif tmp == N:
        ans += 1
        start += 1
print(ans)
