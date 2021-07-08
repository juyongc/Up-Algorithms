import sys
from collections import deque

# BFS 탐색
def bfs():
    q = deque()
    q.append(pos)       # 지훈이 첫 위치 append
    # 불 위치 append
    for i in range(len(fire)):
        q.append(fire[i])
    # 큐 돌리기
    while q:
        x,y,stat = q.popleft()      # 행,열,상태값
        if stat == 'J':                                     # 지훈이라면,
            if maze[x][y] == 'F':                           # 불이 난 위치면 -> continue
                continue
            if x == 0 or x == R-1 or y == 0 or y == C-1:    # 가장자리면 -> 해당 값 + 1 return
                return maze[x][y] + 1
        
        # 4방향 탐색
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<R and 0<=b<C:       # 범위 내에서
                if stat == 'J':         # 지훈이라면
                    if maze[a][b] == '.':               # 해당 위치가 빈 칸이면
                        maze[a][b] = maze[x][y] + 1     # 해당 위치 = 이전 위치값 +1
                        q.append((a,b,'J'))           
                elif stat == 'F':       # 불이라면
                    if maze[a][b] != 'F' and maze[a][b] != '#':     # 해당 위치가 불이나 벽이 아니라면
                        maze[a][b] = 'F'                            # 해당 위치 -> 불로 변경
                        q.append((a,b,'F'))
    
    return 'IMPOSSIBLE'         # 탈출 실패 -> 'IMPOSSIBLE' return


inputs = sys.stdin.readline

R,C = map(int,inputs().split())
maze = [list(inputs().rstrip()) for _ in range(R)]
fire = []   # 불 저장용
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':           # 불 위치 찾기
            fire.append((i,j,'F'))
        elif maze[i][j] == 'J':         # 지훈이 위치 찾기
            pos = ((i,j,'J'))
            maze[i][j] = 0
# 4방향 탐색용
dx = [1,-1,0,0]
dy = [0,0,1,-1]

if pos[0] == 0 or pos[0] == R-1 or pos[1] == 0 or pos[1] == C-1:    # 지훈이가 이미 가장자리라면
    ans = 1
else:                                                               # 아니면
    ans = bfs()
    
print(ans)