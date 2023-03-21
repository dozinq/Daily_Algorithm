import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

ans = [0, 0, 0, 0, 0]
heart = 0
for i in range(N):
    tmp = list(map(str, input()))
    # 심장의 좌표를 찾지 못하였다면,
    if heart == 0:
        if '*' in tmp:
            # 심장의 좌표
            heart = (i+1, tmp.index('*'))
    # 심장을 찾았을 때부터는 다음의 조건을 따른다.
    else:
        # 행 번호가 심장의 좌표일때는 양 팔의 길이를 알 수 있다.
        if i == heart[0]:
            for t in range(N):
                if tmp[t] == '*':
                    # 왼팔의 길이
                    if t < heart[1]:
                        ans[0] += 1
                    # 오른팔의 길이
                    elif t > heart[1]:
                        ans[1] += 1
        # 몸통의 길이
        elif tmp[heart[1]] == '*':
            ans[2] += 1
        else:
            # 왼다리의 길이
            if tmp[heart[1]-1] == '*':
                ans[3] += 1
            # 오른다리의 길이
            if tmp[heart[1]+1] == '*':
                ans[4] += 1

heart = (heart[0]+1, heart[1]+1)
print(*heart)
print(*ans)
