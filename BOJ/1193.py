N = int(input()) # 14

num = 1 
sum_num = 2
num_flag = 0

while(True):
    if N <= num:
        if sum_num % 2 == 0:
            print(f'{sum_num-(N-num_flag)}/{N-num_flag}')
            break
        else:
            print(f'{N-num_flag}/{sum_num-(N-num_flag)}')
            break
    num_flag = num
    num += sum_num
    sum_num += 1