#You may use import as below.
#import math
def check_square(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    return False

def solution(pos):
    # Write code here.
    answer = 0
    pos = (ord(pos[0])-65, int(pos[1])-1)
    move_knight = ((-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-2, 1), (-1, 2))
    for i in range(8):
        if check_square(pos[0]+move_knight[i][0], pos[1]+move_knight[i][1]) == True:
            answer += 1
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")