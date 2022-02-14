# K = 현재 버스의 한계, N = 종점, M = 충전소 정류장 개수
# 인덱스 + K 의 값과 제일 근접한 곳까지 이동하고 ans에 1을 더한다.
# 없다면 0 출력

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station_lst = list(map(int, input().split()))   # 충전소 정류장의 위치를 입력받는다.

    bus = 0                                         # 버스의 현재 위치
    ans = 0                                         # 충전한 횟수

    flag = 1                                        # while문에서 세세한 조건을 설정해주기 위해, 플래그를 1로 설정한다.
    while(flag == 1):                               # while문은 flag가 1이면 계속 실행된다.
        for go in range(K, 0, -1):                  # 최대한 갈 수 있는 충전소 정류장이 있는지 알고 싶었다.
            if bus + go == N:                       # (버스가 현재 위치에서 충전하지 않고 종점에 도착한다면,
                flag = 0                            # while문을 더이상 돌리지 않게 flag를 0으로 설정하고,
                break                               # 일단 for문에서 탈출시킨다.(후에 while문에서도 flag값으로 탈출한다.)
            if bus + go in station_lst:             # 버스가 충전하지 않고 갈 수 있는 충전소 정류장이 있다면,
                bus += go                           # 버스의 현재 위치를 그만큼 조절시킨다.
                ans += 1                            # 충전한 횟수를 1만큼 증가시킨다.
                break                               # 그리고 for문을 탈출시킨다!
        else:                                       # 갈 수 있는 충전소 정류장을 찾다가 실패한다면,
            flag = 0                                # while문까지 탈출시키게끔 flag값을 0으로 만든다.

    if bus + K >= N:                                # 버스가 충전하지 않고도 갈 수 있는 범위가 종점까지의 거리를 초과한다면,
        print(f'#{tc} {ans}')                       # 충전횟수를 출력한다.
    else:                                           # 아니라면,
        print(f'#{tc} 0')                           # 0을 출력한다.