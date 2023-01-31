import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = set(list(input()))
    str2 = input()
    ans =0

    for index in str1:
        cnt = 0
        for j in str2:
            if index in j:
                cnt += 1
        if ans < cnt:
            ans = cnt

    print(f'#{tc} {ans}')