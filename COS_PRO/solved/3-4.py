# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    answer = len(s1) + len(s2)
    min_len = min(len(s1), len(s2))
    for i in range(1, min_len+1):
        if s1[0:i] == s2[-i:]:
            answer = min(answer, len(s1) + len(s2) - i)
        if s1[-i:] == s2[0:i]:
            answer = min(answer, len(s1) + len(s2) - i)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")