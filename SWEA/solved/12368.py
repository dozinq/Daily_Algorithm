import sys
sys.stdin = open('BOJ/input.txt')

for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    if a + b < 24:
        ans = a + b
    else:
        ans = a + b - 24
    print(f'#{tc} {ans}')