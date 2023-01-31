import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stations = [0]*5000
    for _ in range(N):
        A, B = map(int, input().split())
        for index in range(A-1, B):
            if index < len(stations):
                stations[index] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for _ in range(P):
        num = int(input())
        print(stations[num-1], end=' ')
    print()