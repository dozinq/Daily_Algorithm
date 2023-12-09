import sys
sys.stdin = open('CODETREE/input.txt')

def check_square(x, y):
    return True if 0 <= x < L and 0 <= y < L else False

def move_knight(i, d):
    # 움직임 변동 사항을 movement 디렉토리로 관리
    movement = {}

    tmp_move = []
    for r, c in knights[i]:
        nr, nc = r + delta[d], c + delta[d]
        if not check_square(nr, nc):
            return False
        else:
            tmp_move.append(nr, nc)



    return

L, N, Q = map(int, input().split())

# 0: 빈칸, 1: 함정, 2: 벽
data = []
for _ in range(L):
    data.append(list(map(int, input().split())))

# knights에는 인덱스 별 위치가 저장되고, 체력은 knights_hp로 관리한다.
knights = {}
knights_hp = [0]
knights_damage = [0]

for kn in range(N):
    r, c, h, w, k = list(map(int, input().split()))
    knight = []
    for kr in range(r-1, r+h-1):
        for kc in range(c-1, c+w-1):
            knight.append([kr, kc])
    knights[kn+1] = knight
    knights_hp.append(k)

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

for _ in range(Q):
    move_knight(*map(int, input().split()))
