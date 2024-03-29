#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = 0
    data = [0 for _ in range(10001)]
    queue = [number]
    data[number] = 0
    while queue:
        n = queue.pop()
        if n == target:
            break
        if n + 1 <= 10000 and data[n + 1] == 0:
            data[n + 1] = data[n] + 1
            queue.append(n + 1)
        if n - 1 > 0 and data[n - 1] == 0:
            data[n - 1] = data[n] + 1
            queue.append(n - 1)
        if n * 2 <= 10000 and data[n * 2] == 0:
            data[n * 2] = data[n] + 1
            queue.append(n * 2)
    answer = data[target]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")