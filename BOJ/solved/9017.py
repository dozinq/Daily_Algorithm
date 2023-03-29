import sys
sys.stdin = open('BOJ/input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    team = [0 for _ in range(201)]
    team_lst = []

    for i in range(len(data)):
        # 소속 팀원의 수를 누적한다.
        team[data[i]] += 1
        if team[data[i]] == 6:
            team_lst.append(data[i])
    
    ans_lst = [list() for _ in range(len(team_lst))]

    cnt = 1
    for i in range(len(data)):
        if data[i] in team_lst:
            ans_lst[team_lst.index(data[i])].append(cnt)
            cnt += 1

    ans = [0, float('inf')]
    for i in range(len(ans_lst)):
        if ans[1] > sum(ans_lst[i][0:4]):
            ans[1] = sum(ans_lst[i][0:4])
            ans[0] = i
        elif ans[1] == sum(ans_lst[i][0:4]):
            if ans_lst[ans[0]][4] > ans_lst[i][4]:
                ans[1] = sum(ans_lst[i][0:4])
                ans[0] = i

    print(team_lst[ans[0]])
