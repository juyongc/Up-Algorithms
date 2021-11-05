import sys
from collections import deque
inputs = sys.stdin.readline

N,M,K = map(int,inputs().split())
arr = [list(map(int,inputs().split())) for _ in range(N)]

narr = [[arr[i][j] for j in range(M)] for i in range(N)]

q = deque()

sx, sy = 0, 0
row, col = N, M
while not (row == 0 or col == 0):
    # 해당 행/열 값 순서대로 넣기
    for i in range(sy,sy+col):
        q.append(narr[sx][i])
    for i in range(sx+1,sx+row):
        q.append(narr[i][sx+col-1])
    for i in range(sx+col-2,sy,-1):
        q.append(narr[sy+row-1][i])
    for i in range(sy+row-1,sx,-1):
        q.append(narr[i][sy])

    q.rotate(-K)    # K만큼 반시계 회전

    # 해당하는 행/열 값 변경
    for i in range(sy, sy + col):
        now = q.popleft()
        narr[sx][i] = now
    for i in range(sx + 1, sx + row):
        now = q.popleft()
        narr[i][sx + col - 1] = now
    for i in range(sx+col-2, sy, -1):
        now = q.popleft()
        narr[sy+row-1][i] = now
    for i in range(sy + row - 1, sx, -1):
        now = q.popleft()
        narr[i][sy] = now
    sx += 1
    sy += 1
    row -= 2
    col -= 2

for i in range(N):
    print(' '.join(map(str,narr[i])))