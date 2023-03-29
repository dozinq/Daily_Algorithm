import sys, collections
sys.stdin = open('BOJ/input.txt')

N = int(input())

data = collections.deque(i for i in range(1, N+1))
while len(data) > 1:
    data.popleft()
    data.append(data.popleft())
print(*data)