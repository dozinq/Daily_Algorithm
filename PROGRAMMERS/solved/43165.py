def dfs(tmp_sum, depth):
    global answer
    if depth == len(lst):
        if tmp_sum == tar:
            answer += 1
            return 0
    else:
        for i in range(2):
            if i == 0:
                dfs(tmp_sum - lst[depth], depth + 1)
            else:
                dfs(tmp_sum + lst[depth], depth + 1)
        return

def solution(numbers, target):
    global lst, tar, answer
    lst, tar = numbers, target
    answer = 0
    dfs(0, 0)
    return answer