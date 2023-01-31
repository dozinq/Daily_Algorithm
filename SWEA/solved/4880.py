def group(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return game(lst[0], lst[1])
    return game(group(lst[0:(len(lst)-1)//2+1]), group(lst[(len(lst)-1)//2+1:len(lst)]))

def game(a, b):
    if (a[1] % 3) + 1 == b[1]:
        return b
    return a


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(enumerate(map(int, input().split())))
    idx_lst = [[0, 0] for _ in range(N)]

    print(f'#{tc} {group(lst)[0]+1}')