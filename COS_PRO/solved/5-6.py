#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.
    answer = ''
    tmp_s1 = 0
    tmp_s2 = 0
    for i in range(len(s1)):
        tmp_s1 += int(s1[len(s1)-1-i]) * (p**i)
    for j in range(len(s2)):
        tmp_s2 += int(s2[len(s2)-1-j]) * (p**j)
    tmp = tmp_s1 + tmp_s2

    while tmp > 0:
        answer = str(tmp % q) + answer
        tmp //= q
    
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")