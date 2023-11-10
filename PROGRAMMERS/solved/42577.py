def solution(phone_book):
    answer = True
    # phone_book.sort(key=lambda x: len(x))
    # for i in range(1, len(phone_book)):
    #     for j in range(i):
    #         if phone_book[i][0:len(phone_book[j])] == phone_book[j]:
    #             answer = False
    #             break
    
    phone_dict = {}
    for p in phone_book:
        phone_dict[p] = 1
        
    for p in phone_dict:
        tmp = ''
        for i in range(0, len(p)-1):
            tmp += p[i]
            if tmp in phone_dict:
                return False
    return True