def star(lst, n):
    if n > 3:
        
        lst[1][1] = ' '
        return lst

N = int(input())
data = [list('*'*N) for _ in range(N)]
new_lst = star(data, N//3)

for i in range(N):
    print(''.join(new_lst[i]))