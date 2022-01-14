def judgement(j1, j2):
    if ((j1=='가위' and j2=='보') or (j1=='바위' and j2=='가위') or (j1=='보' and j2 == '바위')):
        print('%s가 이겼습니다!' % j1)
    elif ((j1=='바위' and j2=='보') or (j1=='보' and j2=='가위') or (j1=='가위' and j2 == '바위')):
        print('%s가 이겼습니다!' % j2)
    else:
        print('비겼습니다!')

player_a = input()
player_b = input()
a_weapon = input()
b_weapon = input()

judgement(a_weapon, b_weapon)