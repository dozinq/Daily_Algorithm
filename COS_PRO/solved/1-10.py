def solution(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer

#The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3];
ret1 = solution(prices1);

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
prices2 = [3, 1];
ret2 = solution(prices2);

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")