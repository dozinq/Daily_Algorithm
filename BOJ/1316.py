# 단어 개수 N 받기
N = int(input())
# 결과값으로 반환할 total 상자 만들기
total = 0
# 반복문 안에서 한줄씩 검사하기
# 연속되는 부분 건너 뛰기
# 나왔던 단어 나오면 total에 0 누적하고 다시 돌리기


for _ in range(0, N):
    my_str = input()
    my_lst = []
    flag = True

    for index in range(0, len(my_str)-1):
        if my_str[index] == my_str[index +1]:
            continue
        else:
            if my_str[index+1] in my_lst:
                flag = False
                break
            else:
                my_lst.append(my_str[index])
    if my_str[-1] in my_lst:
        flag = False
    if flag:        
        total += 1

print(total)





    # my_str = input()
    # word = list(set(my_str))
    # for index in word:
    #     my_str.count(index)
        


# total 출력하기