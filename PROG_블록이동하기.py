from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1] 
def solution(boards):
    global board
    answer = 0
    N = len(boards)
    # 주변 벽 두르기
    board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            board[i+1][j+1] = boards[i][j]
    
    q = deque()
    q.append([1,1,1,2,0])

    visit = set()   # 방문체크
    
    while q:
        x1,y1,x2,y2,val = q.popleft()
        if (x1 == N and y1 == N) or (x2 == N and y2 == N):
            answer = val
            break
        else:
            if (x1,y1,x2,y2) in visit:
                continue
            else:
                visit.add((x1,y1,x2,y2))
        
        for i in range(4):
            check = move(x1,y1,x2,y2,val,i,N)
            if check:
                q.append(check)
        check = rotate(x1,y1,x2,y2,val,N)
        if check:
            for ch in check:
                q.append(ch)
    return answer
# 이동    
def move(r1,c1,r2,c2,cnt,k,N):
    global board
    nr1 = r1 + dy[k]
    nc1 = c1 + dx[k]
    if board[nr1][nc1] == 1:
        return False
    nr2 = r2 + dy[k]
    nc2 = c2 + dx[k]
    if board[nr2][nc2] == 1:
        return False
    return [nr1,nc1,nr2,nc2,cnt+1]
# 회전
def rotate(r1,c1,r2,c2,cnt,N):
    global board
    poss = []
    if r1 == r2:
        if board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
            poss.append([r1,c1,r1-1,c1,cnt+1])
            poss.append([r2,c2,r2-1,c2,cnt+1])
        if board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
            poss.append([r1,c1,r1+1,c1,cnt+1])
            poss.append([r2,c2,r2+1,c2,cnt+1])
    else:
        if board[r1][c1-1] == 0 and board[r2][c2-1] == 0:
            poss.append([r1,c1,r1,c1-1,cnt+1])
            poss.append([r2,c2,r2,c2-1,cnt+1])
        if board[r1][c1+1] == 0 and board[r2][c2+1] == 0:
            poss.append([r1,c1,r1,c1+1,cnt+1])
            poss.append([r2,c2,r2,c2+1,cnt+1])
    return poss