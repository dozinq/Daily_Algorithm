#You may use import as below.
#import math

def solution(n):
    # Write code here.
    answer = 0
    tor_lst = [[0]*n for _ in range(n)]
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    num = 1
    x, y, d = 0, 0, 0
    while num <= n**2:
        tor_lst[x][y] = num
        if 0 <= x + delta[d][0] < n and 0 <= y + delta[d][1] < n and tor_lst[x + delta[d][0]][y + delta[d][1]] == 0:
            x, y = x + delta[d][0], y + delta[d][1]
        else:
            d = (d+1) % 4
            x, y = x + delta[d][0], y + delta[d][1]
        num += 1
    idx = 0
    while idx < n:
        answer += tor_lst[idx][idx]
        idx += 1

    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")