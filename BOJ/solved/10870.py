def fib(num):
    if num >= 2:
        return fib(num-1) + fib(num-2)
    elif num < 2:
        if num == 0:
            return 0
        return 1
    

n = int(input())
print(fib(n))