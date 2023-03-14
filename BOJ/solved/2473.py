import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = sorted(list(map(int, sys.stdin.readline().split())))

ans = float('inf')
ans_lst = [0, 0, 0]
flag = 0
for i in range(N-2):
    if flag == 1:
        break
    start = i+1
    end = N-1
    while start < end:
        tmp_sum = data[i] + data[start] + data[end]
        if abs(tmp_sum) < ans:
            ans = abs(tmp_sum)
            ans_lst = [data[i], data[start], data[end]]
        if tmp_sum < 0:
            start += 1
        elif tmp_sum > 0:
            end -= 1
        else:
            flag = 1
            break
print(*ans_lst)

