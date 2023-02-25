import sys
sys.stdin = open('BOJ/input.txt')

def N_Queen(cnt):
    global ans, data
    if cnt == N:
        ans += 1
        return
    else:
        for i in range(N):
            if data[cnt][i] == 0:
                data[cnt][i] = 1
                for j in range(cnt+1, N):
                    num = j - cnt
                    if i - num >= 0:
                        data[j][i-num] +=1
                    if i + num < N:
                        data[j][i+num] += 1
                    data[j][i] += 1
                N_Queen(cnt+1)
                data[cnt][i] = 0
                for k in range(cnt+1, N):
                    num = k - cnt
                    if i - num >= 0:
                        data[k][i-num] -= 1
                    if i + num < N:
                        data[k][i+num] -= 1
                    data[k][i] -= 1
        return


N = int(input())
data = [list(0 for _ in range(N)) for _ in range(N)]
ans = 0
N_Queen(0)
print(ans)