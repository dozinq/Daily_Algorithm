max_num = 0
cnt = 1
for i in range(1,10):
    i = int(input())
    if max_num < i:
        max_num = i
        my_cnt = cnt
    cnt += 1

print(max_num)
print(my_cnt)