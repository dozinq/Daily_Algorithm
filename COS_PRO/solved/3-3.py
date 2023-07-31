#다음과 같이 import를 사용할 수 있습니다.
#import math

def check_square(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    return False

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0
    chess = [[0]*8 for _ in range(8)]
    delta = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for i in range(len(bishops)):
        r, c = ord(bishops[i][0])-65, int(bishops[i][1])-1
        chess[r][c] = 1
        for d in range(4):
            mtp = 1
            while mtp <= 8:
                nr, nc = r + (delta[d][0] * mtp), c + (delta[d][1] * mtp)
                if check_square(nr, nc):
                    if chess[nr][nc] == 0:
                        chess[nr][nc] = 1
                    mtp += 1
                else:
                    break
    for x in range(8):
        for y in range(8):
            if chess[x][y] == 0:
                answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")