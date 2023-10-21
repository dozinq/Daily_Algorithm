def solution(s):
    answer = ''
    # 0번째 인덱스를 제외하고는 모든 단어는 스페이스 뒤에 위치할 것므로,
    answer = s[0].upper()
    
    for w in range(1, len(s)):
        # 현재 인덱스가 공백문자가 아닌가
        if s[w] != ' ':
            # 이전 인덱스가 공백문자였나 (== 단어의 첫문자인가)
            if s[w-1] == ' ':
                answer += s[w].upper()
            # 단어의 첫 문자가 아닌데 대문자라면,
            elif s[w].isupper():
                answer += s[w].lower()
            # 단어의 첫 문자가 아닌데 대문자도 아니라면,
            else:
                answer += s[w]
        # 현재 인덱스가 공백문자라면 그대로 공백 처리
        else:
            answer += s[w]

    return answer