import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())
data = {}

for _ in range(N):
    tmp = sys.stdin.readline().strip()
    if len(tmp) >= M:
        # flag는 찾았는지에 대한 여부이며, 이에 따라 추가하는 방식이 달라진다.
        if tmp in data:
            data[tmp] += 1
        else:
            data[tmp] = 1

data = sorted(data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in data:
    print(i[0])