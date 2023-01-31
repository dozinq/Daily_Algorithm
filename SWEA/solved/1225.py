"""
한 사이클 당 5까지 감소.
0보다 작아지는 경우 0으로 저장되며 그때의 배열 출력
(테스트 케이스의 값이 주어져있지 않아서, 임의로 10이라고 입력해보고 실행)
"""
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    data.append(0)                          # 9자리의 배열 생성! (9번째 자리는 임시 저장 공간!)
    while(data[7] > 0):
        for n in range(1, 6):
            data[0] -= n
            data[8] = data[0]
            for i in range(8):
                data[i] = data[i+1]
            if data[7] <= 0:
                data[7] = 0
                break
    data.pop()
    print(f'#{tc}', end=' ')
    for index in data:
        print(index, end=' ')
    print()