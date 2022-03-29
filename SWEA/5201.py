T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    freights.sort()
    trucks.sort()

    ans = 0
    while (len(freights) > 0 and len(trucks) > 0):      # 남은 화물이나 트럭이 없을 때까지 반복!
        freight = freights.pop()    # 현재 화물을 빼서~
        if freight <= trucks[-1]:   # 현재 남은 트럭 중에 화물을 가져갈 수 있다면,
            ans += freight          # ans에 화물을 누적!
            trucks.pop()            # 화물을 가져간다면, 그 트럭에 짐을 싣고 제외시키자!
    print(f'#{tc} {ans}')
