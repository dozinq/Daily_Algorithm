def heap(node):
    if node // 2 > 0:
        if ans_lst[(node//2)-1] > ans_lst[node-1]:
            ans_lst[node-1], ans_lst[(node//2)-1] = ans_lst[(node//2)-1], ans_lst[node-1]
            heap(node//2)

def maxpar(son):
    if son//2 > 0:
        return ans_lst[(son//2)-1] + maxpar(son//2)
    else:
        return 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans_lst = []

    while(1):
        tmp = data.pop(0)
        ans_lst.append(tmp)
        heap(len(ans_lst))
        if len(data) == 0:
            break
    print(f'#{tc} {maxpar(len(ans_lst))}')