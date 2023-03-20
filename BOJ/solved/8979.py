import sys
sys.stdin = open('BOJ/input.txt')

# 입력 : 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, input().split())

# data 배열은 N 만큼의 길이를 가진다.
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

data.sort(key=lambda x: x[0])

# data 배열을 순회하면서 등수를 알고 싶은 국가 K 보다 높은지만 확인하고, 그렇다면 ans에 누적한다.
ans = 1
for i in range(N):
    if i == K-1:
        continue
    else:
        if data[i][1] > data[K-1][1]:
            ans += 1
        elif data[i][1] == data[K-1][1]:
            if data[i][2] > data[K-1][2]:
                ans += 1
            elif data[i][2] == data[K-1][2]:
                if data[i][3] > data[K-1][3]:
                    ans += 1

print(ans)