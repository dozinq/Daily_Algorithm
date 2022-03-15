def star(lst, n):
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            lst[i][j] = ' '
    if n > 1:
        for i in range(0, len(lst), n): # 0 9 3
            for j in range(0, len(lst), n):
                if i == n and j == n:
                    continue
                else:
                    new_lst = []
                    new_lst[i][j:j+n] = lst[i][j:j+n]
                    star(new_lst, n//3)
    return lst

N = int(input())
data = [list('*'*N) for _ in range(N)]
new_lst = star(data, N//3)

for i in range(N):
    print(''.join(new_lst[i]))