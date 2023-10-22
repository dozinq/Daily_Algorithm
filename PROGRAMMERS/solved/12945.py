# def fibo(n):
#     if n <= 1:
#         return n        
#     return fibo(n-1) + fibo(n-2)

def solution(n):
    answer = 0
    memo = [0, 1, 1, 2, 3, 5]
    if n > 5:
        num = 6
        while num <= n:
            memo.append(memo[num-1] + memo[num-2])
            num += 1
    answer = memo[n] % 1234567
    # answer = fibo(n) % 1234567
    return answer