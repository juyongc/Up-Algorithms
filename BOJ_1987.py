import sys

# dbs 탐색
def dfs(x,y,cur):
    global maxi
    for k in range(4):
        r,c = x+dx[k],y+dy[k]
        if 0<=r<R and 0<=c<C:
            now = plate[r][c]
            # 현재까지 없던 알파벳이면
            if now not in alpha[x][y]:
                alpha[x][y].add(plate[r][c])        # set에 삽입
                if alpha[r][c] != alpha[x][y]:      # 중복 방문 방지
                    alpha[r][c] = set(alpha[x][y])      # [r][c]번째 set 갱신!
                    dfs(r,c,cur+1)                      # 다음 dfs
                    maxi = max(maxi, cur+1)             # 최대값 비교
                alpha[x][y].discard(plate[r][c])    # 이전 상태로 되돌리기 위한 삭제

inputs = sys.stdin.readline
R,C = map(int,inputs().split())
plate = [list(inputs().rstrip()) for _ in range(R)]
alpha = [[set() for _ in range(C)] for _ in range(R)]   # 위치별 set
# 4방향 탐색
dx = [1,-1,0,0]
dy = [0,0,1,-1]

alpha[0][0].add(plate[0][0])
maxi = 1
dfs(0,0,1)
print(maxi)