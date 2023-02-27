import sys
sys.stdin = open('BOJ/input.txt')

def N_Queen(cnt):
    global ans, data
    if cnt == N:
        ans += 1
        return
    else:
        for i in range(N):
            flag = 0
            for prev in range(cnt):
                if data[prev] == i or abs(i-data[prev]) == cnt-prev:
                    flag = 1
                    break
            if flag == 0:
                data[cnt] = i
                N_Queen(cnt+1)
                
    return

N = int(input())
data = [0 for _ in range(N)]
ans = 0
N_Queen(0)
print(ans)