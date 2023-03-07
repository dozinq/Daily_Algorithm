import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = list(map(int, input().split()))

ans = 0
for num in data:
    flag = 0
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                flag += 1
            if flag == 2:
                break
    if flag == 1:
        ans += 1

print(ans)
