import sys
inputs = sys.stdin.readline

# 선마다 자기 자신이 나오는지 체크
def check():

    for cx in range(1,N+1):
        start = cx
        for cy in range(1,H+1):
            if ladder[cy][start] == 1:
                start += 1
            elif start > 0 and ladder[cy][start-1] == 1:
                start -= 1
        if start != cx:
            return False
    return True

# DFS
def dfs(x,y,cnt):
    global ans
    if cnt >= ans:
        return
    if cnt > 3:
        return
    if check():     # 모든 선 자기자신 나오는 지 체크
        ans = min(ans,cnt)
        return

    for i in range(x,H+1):
        if i == x:  # 같은 열이면 자신 위치부터 시작하기
            k = y
        else:
            k = 1
        # 가로선 만들기
        for j in range(k,N):
            if ladder[i][j] == 0:
                ladder[i][j] = 1
                dfs(i,j+2,cnt+1)
                ladder[i][j] = 0


N,M,H = map(int,inputs().split())

ladder = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    r,c = map(int,inputs().split())
    ladder[r][c] = 1

ans = 4
dfs(0,0,0)

if ans == 4:
    ans = -1

print(ans)