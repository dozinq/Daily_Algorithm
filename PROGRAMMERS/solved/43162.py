# find 함수는 자신과 연결되어 있는 최저점을 찾아준다.
def find(node):
    if not parents[node] == node:
        return find(parents[node])
    return node

def union(x, y):
    global parents
    a, b = find(x), find(y)
    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b
    return

def solution(n, computers):
    global parents
    answer = 0
    # parents 리스트 초기화
    parents = list(i for i in range(len(computers)))
    
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if computers[i][j] == 1:
                union(i, j)
    
    tmp_lst = []
    for i in range(len(parents)):
        par = find(i)
        if par not in tmp_lst:
            tmp_lst.append(par)
            answer += 1
        
    return answer