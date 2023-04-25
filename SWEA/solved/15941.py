import sys
sys.stdin = open('BOJ/input.txt')

for tc in range(1, int(input())+1):
    tmp = int(input())
    print(f'#{tc} {tmp**2}')