import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
# data는 N만큼 입력을 받는다.
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans_lst = []
for i in range(len(data)):
    tmp = 1
    for j in range(len(data)):
        # 자신이라면, 무시한다.
        if i == j:
            continue
        # 자신보다 몸무게와 키가 둘 다 크다면 등수는 하나 더해진다.
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            tmp += 1
    ans_lst.append(tmp)

print(*ans_lst)