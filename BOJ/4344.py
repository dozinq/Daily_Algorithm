C = int(input())
for i in range(C):
    A = list(map(int, input().split()))
    avg = (sum(A[1:]) / A[0])
    count = 0

    for j in A[1:]:
        if j > avg:
            count += 1
    rate = (count / A[0]) * 100
    print('%.3f' % rate, end=''), print('%')