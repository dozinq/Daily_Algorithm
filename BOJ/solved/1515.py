import sys
sys.stdin = open('BOJ/input.txt')

num = input()

i = 1
flag = 0
while flag == 0:
    for idx in str(i):
        if idx == num[0]:
            if len(num) > 1:
                num = num[1:]
            else:
                flag = i
    i += 1
    
print(flag)
