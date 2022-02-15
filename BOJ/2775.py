T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    lst = [number for number in range(1, n+1)] # lst에 1~n까지 담김
    
    # k층의 n호 사람 수를 구하면 된다.
    for num_k in range(k): 
        for num_n in range(1, n): # 1 ~ n-1 인덱스 까지 반복한다.
            # 층이 올라갈수록 2호는 1호값에 현재값을 더하고, 3호는 2호값에 현재값을 더한다.
            lst[num_n] += lst[num_n-1]
            # num_n-1 즉, 인덱스에 값이 담기게 됨

    print(lst[-1])        

        
    # 1층이 되면 1호는 1, 2호는 1+2, 3호는 1+2+3, 4호는 1+2+3+4 의 값을 갖는다.

    # k-1층에 도달하였을때, ans변수에 1~n호의 현재값을 누적시킨다.
        


    # 1 5 15 35 70    1 + 5 + 15 + 35
    # 1 4 10 20 35    1 + 1+4 + 1+4+10 + 1+4+10+20
    # 1 3  6 10 15  1 + 1+1+3 + 1+1+3+1+3+6 + 1+1+3+1+3+6+1+3+6+10
    # 1 2 3  4  5   1 + 1+1+1+2 + 1+1+1+2+1+1+2+1+2+3+ 1+