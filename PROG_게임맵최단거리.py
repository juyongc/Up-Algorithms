from collections import deque
def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    answer = bfs(0,0,row,col,maps)
    return answer

# bfs 탐색
def bfs(sx,sy,r,c,arr):
    q = deque()
    q.append((sx,sy))
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visit =[[-1]*c for _ in range(r)]
    visit[sx][sy] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<r and 0<=b<c and arr[a][b] == 1 and visit[a][b] == -1:
                visit[a][b] = visit[x][y] + 1   # 이전값 + 1
                q.append((a,b))
            if a == r-1 and b == c-1:
                return visit[a][b]
    return -1