import sys
inputs = sys.stdin.readline
from collections import deque


N,M,X,Y,K = map(int,inputs().split())
# 바닥,동,서,북,남
mymap = [list(map(int, input().split())) for _ in range(N)]
order = deque(map(int,inputs().split()))
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

dice = [0]*6
lx,ly = X,Y

while order:
    move = order.popleft()
    r,c = lx + dx[move], ly + dy[move]
    if 0 > r or 0 > c or r > N-1 or c > M-1:
        continue
    # 동,서,북,남별 주사위 위치 변경
    if move == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif move == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif move == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if mymap[r][c] == 0:
        mymap[r][c] = dice[-1]
    else:
        dice[-1] = mymap[r][c]
        mymap[r][c] = 0
    lx,ly = r,c
    print(dice[0])
