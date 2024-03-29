#다음과 같이 import를 사용할 수 있습니다.
#import math
def check_square(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def check_garden(n, garden):
    flag = 0
    for i in range(n):
        if flag == 0:
            for j in range(n):
                if garden[i][j] == 0:
                    flag = 1
                    return flag
    return flag

def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while check_garden(n, garden):
        for i in range(n):
            for j in range(n):
                if garden[i][j] == 1:
                    for d in delta:
                        r, c = i+d[0], j+d[1]
                        if check_square(r, c, n):
                            garden[r][c] = 1
        answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")