from collections import deque

# 상황별 회전 
def rotate(r1,r2,cost):
    global nboard,q,visit
    
    x1,y1 = r1
    x2,y2 = r2
    
    dr = [1,-1]
    check = []    
    if x1 == x2:    # 가로 방향 - 각각 위,아래의 왼쪽, 오른쪽 좌표 0인지 확인
        for i in range(2):
            if nboard[x1+dr[i]][y1] == 0 and nboard[x2+dr[i]][y2] == 0:
                check.append(((x1,y1),(x1+dr[i],y1)))
                check.append(((x2,y2),(x2+dr[i],y2)))
    elif y1 == y2:  # 세로 방향 - 각각 왼쪽,오른쪽의 왼쪽, 오른쪽 좌표 0인지 확인
        for i in range(2):
            if nboard[x1][y1+dr[i]] == 0 and nboard[x2][y2+dr[i]] == 0:
                check.append(((x1,y1),(x1,y1+dr[i])))
                check.append(((x2,y2),(x2,y2+dr[i])))
    # 방문 체크
    for c in check:
        if c not in visit:
            q.append((c,cost+1))
            visit.add(c)
    
    
def solution(board):
    global nboard,q,visit
    
    answer = 0
    N = len(board)
    nboard = [[1]*(len(board)+2) for _ in range(len(board)+2)]  # 테두리 1로 감싸기
    for i in range(len(board)):
        nboard[i+1] = [1] + board[i] + [1]
    # 상,하,좌,우
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque()
    visit = set()
    
    q.append((((1,1),(1,2)),0))     # ((왼쪽 좌표, 오른쪽 좌표), cost값)
    visit.add(((1,1),(1,2)))
    
    while q:
        loc, cost = q.popleft()
        lx,ly,rx,ry = loc[0][0],loc[0][1],loc[1][0],loc[1][1]
        if (lx,ly) == (N,N) or (rx,ry) == (N,N):    # 마지막 위치 들어왔으면 STOP
            answer = cost
            break
        # 상,하,좌,우 확인 - 왼쪽, 오른쪽 좌표 모두 1이 아니면 q에 추가
        for k in range(4):
            lx_next,ly_next = lx + dx[k], ly + dy[k]
            rx_next,ry_next = rx + dx[k], ry + dy[k]
            if nboard[lx_next][ly_next] == 0 and nboard[rx_next][ry_next] == 0:
                if ((lx_next,ly_next),(rx_next,ry_next)) not in visit:
                    q.append((((lx_next,ly_next),(rx_next,ry_next)),cost+1))
                    visit.add(((lx_next,ly_next),(rx_next,ry_next)))
        rotate(loc[0],loc[1],cost)  # 시계, 반시계방향 회전
        
    return answer