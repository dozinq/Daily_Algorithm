N = int(input())

for i in range(N):
    A = str(input())
    count = 0
    ans = 0
    for j in A:
        if j == 'O':
            count += 1
            ans += count
        elif j == 'X':
            count = 0
    print(ans)