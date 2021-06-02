import sys
from collections import deque


def move():
    global sx,sy,fx,fy
    q = deque()
    q.append((sx-1,sy-1,0))

    while q:
        x,y,cnt = q.popleft()
        if x == fx-1 and y == fy-1:
            return cnt
        for k in range(4):
            r = x + dx[k]
            c = y + dy[k]
            if 0<=r<N and 0<=c<M and visit[r][c] == 0:
                visit[r][c] = 1
                check = 0
                # 상황별 다르게
                # k == 0 이면,
                # (마지막 row + 1) 의 column 값들이 범위 내에 있고 벽에 부딪치지 않아야 함
                if k == 0:
                    if 0<=r+H-1<N:
                        for i in range(W):
                            if rec[r+H-1][c+i] == 1:
                                check = 1
                                break
                        if check == 0:
                            q.append((r,c,cnt+1))
                # k == 1이면,
                # (맨 위 row + 1)의 column 값들이 범위 내이고, 벽에 부딪치지 않아야 함
                elif k == 1:
                    for i in range(W):
                        if rec[r][c+i] == 1:
                            check = 1
                            break
                    if check == 0:
                        q.append((r,c,cnt+1))
                # k == 2이면,
                # (오른쪽 column + 1)의 row 값들이 범위 내이고, 벽에 부딪치지 않아야 함
                elif k == 2:
                    if 0<=c+W-1<M:
                        for i in range(H):
                            if rec[r+i][c+W-1] == 1:
                                check = 1
                                break
                        if check == 0:
                            q.append((r,c,cnt+1))
                # k == 3이면,
                # (왼쪽 column + 1)의 row 값들이 범위 내이고, 벽에 부딪치지 않아야 함
                else:
                    for i in range(H):
                        if rec[r+i][c] == 1:
                            check = 1
                            break
                    if check == 0:
                        q.append((r,c,cnt+1))

    return -1

inputs = sys.stdin.readline

N,M = map(int,inputs().split())
rec = [list(map(int,inputs().split())) for _ in range(N)]
H,W,sx,sy,fx,fy = map(int,inputs().split())
visit = [[0]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = move()

print(ans)