T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start = (N-1)//2
    data = [list(map(int, input())) for _ in range(N)]
    
    ans = sum(data[start])
    i = 1
    while i < N-i:
        ans += sum(data[start-i][0+i:N-i])
        ans += sum(data[start+i][0+i:N-i])
        i += 1
    print(f'#{tc} {ans}')
