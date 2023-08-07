#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(K, words):
    #여기에 코드를 작성해주세요.
    answer = 0
    words = list(map(len, words))
    idx = 0
    while idx < len(words):
        lim = K - words[idx]
        answer += 1
        idx += 1
        while idx < len(words):
            if lim - 1 - words[idx] >= 0:
                lim -= (1 + words[idx])
                idx += 1
            else:
                break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")