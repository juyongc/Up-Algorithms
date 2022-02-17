from collections import deque
# 길 만들기 => 테두리:1 / 내부:2 / 외부:0
def make_road(x1,y1,x2,y2):
    global road
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i == x1 or i == x2) and road[j][i] != 2:
                road[j][i] = 1
            elif (j == y1 or j == y2) and road[j][i] != 2:
                road[j][i] = 1
            else:
                road[j][i] = 2
    
# 테두리만 찾아서 증가시키기
def bfs(sx,sy,ex,ey):
    global road
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque()
    visit = [[0]*102 for _ in range(102)]
    q.append((sx,sy))
    visit[sy][sx] = 1
    
    while q:
        a,b = q.popleft()
        for k in range(4):
            x,y = a+dx[k],b+dy[k]
            if (x,y) == (ex,ey):
                return visit[b][a] // 2
            if visit[y][x] == 0 and road[y][x] == 1:
                visit[y][x] = visit[b][a] + 1
                q.append((x,y))
    
            
def solution(rectangle, characterX, characterY, itemX, itemY):
    global road
    answer = 0
    # 인접으로 인한 최단거리 오류를 없애기 위해 2배로 늘리기
    road = [[0]*102 for _ in range(102)]
    
    for rect in rectangle:
        x1,y1,x2,y2 = rect
        make_road(x1*2,y1*2,x2*2,y2*2)
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2)
    
    return answer