from collections import deque
def solution(m, n, puddles):
    answer = 0
    avoid = [[0]*m for _ in range(n)]
    for val in puddles:
        y,x = val[0]-1,val[1]-1
        avoid[x][y] = 1
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    if avoid[0][1] == 0:
        q.append([0,1])
    if avoid[1][0] == 0:
        q.append([1,0])
    while q:
        x,y = q.popleft()
        # 이미 합한 전적이 있으면 continue
        if visit[x][y] != 0:
            continue
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<n and 0<=b<m and avoid[a][b] == 0:
                if k == 0 or k == 2:        # 우/하면
                    if visit[a][b] == 0:    # 방문한적 없으면 append
                        q.append([a,b])
                else:                           # 좌/상이면
                    visit[x][y] += visit[a][b]  # 더하기
    answer = visit[n-1][m-1] % 1000000007       # 결과값
    return answer