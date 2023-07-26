#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = ''
    for n in str(num+1):
        if n == '0':
            answer += '1'
        else:
            answer += n
    answer = int(answer)
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")