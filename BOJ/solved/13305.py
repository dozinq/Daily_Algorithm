import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))

ans = 0
idx = 0
while idx < len(oil)-1:
    # flag는 기름을 충전하였는지 여부를 확인할 수 있다.
    flag = 0
    # 다음 행선지부터 종료지점까지의 주유소를 탐색한다.
    for j in range(idx+1, len(oil)-1):
        # 다음 경로에 더 싼 주유소가 있다면, 지금 주유소에서 갈 수 있는 만큼의 기름을 충전한다.
        if oil[idx] > oil[j]:
            ans += oil[idx] * sum(road[idx:j])
            idx = j
            flag = 1
            break
    # flag가 0이라는 것은 다음 행선지에는 더 이상 더 저렴한 주유소가 없다는 것이기에 종료지점까지 갈 수 있는 기름을 모두 채운다.
    if flag == 0:
        ans += oil[idx] * sum(road[idx:])
        idx = len(oil)-1
print(ans)