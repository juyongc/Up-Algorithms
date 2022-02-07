def solution(grid):
    answer = []
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    # 좌,우 이동시 dx,dy 인덱스
    left = [2,3,1,0]
    right = [3,2,0,1]
    row = len(grid)
    col = len(grid[0])
    # 방문 체크용
    visit = [[[0]*4 for _ in range(col)] for _ in range(row)]
    # 행,열,상하좌우 시작점
    for i in range(row):
        for j in range(col):
            for k in range(4):
                if visit[i][j][k]:
                    continue
                cnt = 1
                px,py,d = i,j,k
                visit[px][py][d] = 1
                # 방문 지점 재방문할 때까지 확인
                while True:
                    nx,ny = px+dx[d],py+dy[d]
                    # 범위 초과시, 조정해주기
                    if nx < 0 or nx >= row:
                        nx = (row+nx)%row
                    if ny < 0 or ny >= col:
                        ny = (col+ny)%col
                    # grid 값별 상하좌우 변경
                    if grid[nx][ny] == "S":
                        nd = d
                    elif grid[nx][ny] == "L":
                        nd = left[d]
                    else:
                        nd = right[d]
                    # 미방문지면 => 방문 체크 / 재방문이면 => 정답 추가
                    if visit[nx][ny][nd] == 0:
                        visit[nx][ny][nd] = 1
                        cnt += 1
                        px,py,d = nx,ny,nd
                    else:
                        answer.append(cnt)
                        break
    answer.sort()
    return answer