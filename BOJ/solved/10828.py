import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
ans = []
for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0][0:3] == 'pus':
        ans.append(int(tmp[1]))
    elif tmp[0][0:3] == 'pop':
        print(-1) if len(ans) == 0 else print(ans.pop())
    elif tmp[0][0:3] == 'siz':
        print(len(ans))
    elif tmp[0][0:3] == 'emp':
        print(1) if len(ans) == 0 else print(0)
    elif tmp[0][0:3] == 'top':
        print(ans[-1]) if len(ans) != 0 else print(-1)
