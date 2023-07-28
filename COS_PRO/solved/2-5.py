"""
코드 리뷰 결과 dp로 풀이하는 것이 더욱 완벽할 듯.
"""

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.
    answer = 1
    tmp = 1
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            tmp += 1
            answer = max(answer, tmp)
        else:
            tmp = 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")