def solution(brown, yellow):
    answer = []
    x = 0
    tmp_sum = (brown - 4)//2

    for i in range(tmp_sum):
        if i * (tmp_sum-i) == yellow:
            ans = max(i, tmp_sum-i)
            break

    answer = [ans + 2, tmp_sum - ans + 2]            

    return answer