def solution(n, words):
    answer = [0, 0]
    pre_words = [words[0]]
    for i in range(1, len(words)):
        if words[i] in pre_words or words[i-1][-1] != words[i][0]:
            answer = [(i%n)+1, (i//n)+1]
            break
        else:
            pre_words.append(words[i])

    return answer