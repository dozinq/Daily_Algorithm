import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def rotate_90(len, x, y):
    return y, (len-1)-x

def art_test():
    # group_art는 그룹을 나타내는 숫자들이 적혀있는 새로운 배열이다.
    group_art = [list(0 for _ in range(n)) for _ in range(n)]
    # group_art에서의 숫자들(그룹)이 실제로는 몇점인지 적혀있다. (0: 실제 점수, 1: 그룹원 수)
    group_score = [0]
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    group_num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                group_score.append([data[i][j], 0])
                group_num += 1
                stack = [(i, j)]
                while stack:
                    tmp = stack.pop()
                    if visited[tmp[0]][tmp[1]] == 0:
                        visited[tmp[0]][tmp[1]] = 1
                        group_art[tmp[0]][tmp[1]] = group_num
                        group_score[group_num][1] += 1
                        for d in range(4):
                            if check_square(tmp[0]+delta[d][0], tmp[1]+delta[d][1]) == True:
                                if visited[tmp[0]+delta[d][0]][tmp[1]+delta[d][1]] == 0:
                                    if data[tmp[0]+delta[d][0]][tmp[1]+delta[d][1]] == data[i][j]:
                                        stack.append((tmp[0]+delta[d][0], tmp[1]+delta[d][1]))
    # 만들어진 group_art에서 각 그룹끼리 닿아있는 지점에 대해 파악한다.
    group_friendship = [0]
    for _ in range(group_num):
        group_friendship.append([0] * (group_num+1))
    for i in range(n):
        for j in range(n):
            # 오른쪽과 아래쪽에 대해서만 파악하면 겹치는 선의 개수를 정확하게 구할 수 있다.
            for d in range(2):
                if check_square(i+delta[d][0], j+delta[d][1]) == True:
                    if group_art[i][j] != group_art[i+delta[d][0]][j+delta[d][1]]:
                        group_friendship[group_art[i][j]][group_art[i+delta[d][0]][j+delta[d][1]]] += 1
                        group_friendship[group_art[i+delta[d][0]][j+delta[d][1]]][group_art[i][j]] += 1
    # 인접한 그룹쌍의 조화로움 값을 모두 더한다.
    tmp_sum = 0
    for i in range(1, group_num+1):
        for j in range(1, group_num+1):
            if group_friendship[i][j] > 0:
                tmp_sum += (group_score[i][1] + group_score[j][1]) * group_score[i][0] * group_score[j][0] * group_friendship[i][j]
                group_friendship[i][j] = 0
                group_friendship[j][i] = 0
    
    # group_art는 그룹을 나타내는 숫자들이 적혀있는 새로운 배열이다.
    # group_score는 숫자들(그룹)이 실제로는 몇점인지 적혀있다. (0: 실제 점수, 1: 그룹원 수)
    
    return tmp_sum

def turn_art():
    global data
    new_art = [list(0 for _ in range(n)) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 십자 모양 컨트롤
            if i == (n-1) // 2 or j == (n-1) // 2:
                if i < (n-1) // 2 and j == (n-1) // 2:
                    tmp_dist = ((n-1) // 2) - i
                    new_art[i+tmp_dist][j-tmp_dist] = data[i][j]
                elif i == (n-1) // 2 and j < (n-1) // 2:
                    tmp_dist = ((n-1) // 2) - j
                    new_art[i+tmp_dist][j+tmp_dist] = data[i][j]
                elif i > (n-1) // 2 and j == (n-1) // 2:
                    tmp_dist = i - ((n-1) // 2)
                    new_art[i-tmp_dist][j+tmp_dist] = data[i][j]
                elif i == (n-1) // 2 and j > (n-1) // 2:
                    tmp_dist = j - ((n-1) // 2)
                    new_art[i-tmp_dist][j-tmp_dist] = data[i][j]
                else:
                    new_art[i][j] = data[i][j]
            # 사각 컨트롤
            else:
                tmp_dist = n//2
                # 2사분면
                if i < (n-1) // 2 and j < (n-1) // 2:
                    new_i, new_j = rotate_90(tmp_dist, i, j)
                    new_art[new_i][new_j] = data[i][j]
                    # new_art[j][(tmp_dist-1)-i] = data[i][j]
                # 3사분면
                elif i > (n-1) // 2 and j < (n-1) // 2:
                    new_i, new_j = rotate_90(tmp_dist, i-(n+1)//2, j)
                    new_art[new_i+(n+1)//2][new_j] = data[i][j]
                    # i, j -> i-(n+1)//2, j -> j, (tmp_dist-1)-(i-(n+1)//2) -> 
                    # new_art[j+(n+1)//2][(tmp_dist-1)-(i-(n+1)//2)] = data[i][j]
                # 4사분면
                elif i > (n-1) // 2 and j > (n-1) // 2:
                    new_i, new_j = rotate_90(tmp_dist, i-(n+1)//2, j-(n+1)//2)
                    new_art[new_i+(n+1)//2][new_j+(n+1)//2] = data[i][j]
                    # i, j -> i-(n+1)//2, j-(n+1)//2 -> j-(n+1)//2, (tmp_dist-1)-(i-(n+1)//2) ->
                    # new_art[j][(tmp_dist-1)-(i-(n+1)//2)+(n+1)//2] = data[i][j]
                # 1사분면
                elif i < (n-1) // 2 and j > (n-1) // 2:
                    new_i, new_j = rotate_90(tmp_dist, i, j-(n+1)//2)
                    new_art[new_i][new_j+(n+1)//2] = data[i][j]
                    # new_art[j - (n+1)//2][(tmp_dist-1) - i + (n+1)//2] = data[i][j]
    data = new_art
    return

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

ans = 0
ans += art_test()
for _ in range(3):
    turn_art()
    ans += art_test()
print(ans)