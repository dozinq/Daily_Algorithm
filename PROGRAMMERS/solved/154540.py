def check_square(x, y, l1, l2):
    if 0 <= x < l1 and 0 <= y < l2:
        return True
    return False

def dfs(x, y, data):
    tmp = 0
    stack = [(x, y)]
    while stack:
        a, b = stack.pop()
        if data[a][b] != 'X':
            tmp += data[a][b]
            data[a][b] = 'X'
            for d in range(4):
                r, c = a + delta[d][0], b + delta[d][1]
                if check_square(r, c, len(data), len(data[0])) == True:
                    if data[r][c] != 'X':
                        stack.append((r, c))
    return tmp

def solution(maps):
    global delta
    answer = []
    data = [list(0 for _ in range(len(maps[0]))) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                data[i][j] = int(maps[i][j])
            else:
                data[i][j] = maps[i][j]
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 'X':
                answer.append(dfs(i, j, data))
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer