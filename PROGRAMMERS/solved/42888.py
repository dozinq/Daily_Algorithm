def search_nick(string):
    nick = ""
    for idx in range(len(string)-1, -1, -1):
        # 공백의 ord 값은 32
        if ord(string[idx]) == 32:
            break
        nick += string[idx]
    # string 뒤집기
    nick = nick[::-1]
    return nick

def search_id(string):
    ids = ""
    flag = 0
    for idx in range(len(string)):
        # 공백의 ord 값은 32
        if ord(string[idx]) == 32:
            if flag == 1:
                break
            flag = 1
        elif flag == 1:
            ids += string[idx]
    return ids

def solution(record):
    answer = []
    nick_dict = {}
    
    # record에서 Enter와 Leave만을 구분하여, ID와 함께 answer에 1차적으로 담는다.
    for idx in range(len(record)):
        if record[idx][0] == "E":
            tmp = search_id(record[idx])
            answer.append("E" + tmp)
            # 나갔다 들어오더라도 아래의 구문을 활용하여 업데이트가 가능하다.
            nick_dict[tmp] = search_nick(record[idx])
        elif record[idx][0] == "L":
            tmp = search_id(record[idx])
            answer.append("L" + tmp)
        else:
            tmp = search_id(record[idx])
            nick_dict[tmp] = search_nick(record[idx])
    # answer를 탐색하며 nick_dict에 해당하는 nickname으로 변경해준다.
    for idx in range(len(answer)):
        if answer[idx][0] == "E":
            answer[idx] = nick_dict[answer[idx][1:]] + "님이 들어왔습니다."
        else:
            answer[idx] = nick_dict[answer[idx][1:]] + "님이 나갔습니다."
            
    return answer