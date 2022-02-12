for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while(dump > 0):
        max_box = max_box_index = min_box_index = 0
        min_box = 100
        index = 0
        for box in boxes:
            if max_box <= box:
                max_box = box
                max_box_index = index
            if min_box >= box:
                min_box = box
                min_box_index = index
            index += 1
        boxes[max_box_index] -= 1
        boxes[min_box_index] += 1
        dump -= 1

    max_box = 0                             # 평탄화 후에 다시 최고점과 최저점의 차를 구해야하므로 한 번 더 구현해 주었다.
    min_box = 100
    for box in boxes:
        if max_box <= box:
            max_box = box
        if min_box >= box:
            min_box = box
    print(f'#{tc} {max_box - min_box}')