N = int(input())

lst = list(map(int, input().split()))
M = int(input())
for i in range(M):
    gen, num = map(int, input().split())
    
    if gen == 1:
        for j in range(1, N+1):
            if j % num == 0:
                lst[j-1] = lst[j-1] ^ 1
    elif gen == 2:
        index = num-1
        lst[index] = lst[index] ^ 1
        a = 1
        while (index-a >= 0 and index+a < N):
            if lst[index-a] ^ lst[index+a] == 0:
                a += 1
            else:
                break
        for j in range(1, a):
            lst[index-j] = lst[index-j] ^ 1
            lst[index+j] = lst[index+j] ^ 1

for i in range(len(lst)):
    print(lst[i], end=' ')
    if i != 0 and (i+1) % 20 == 0:
        print()