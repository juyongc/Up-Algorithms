import sys
from collections import deque
inputs = sys.stdin.readline

# 모든 조합 찾기
def dfs(tot,n,loc):
    if loc >= 3:
        orders.append(now[:])
        return
    for i in range(n,tot):
        now[loc] = i
        dfs(tot,i+1,loc+1)

# 죽인 수 카운팅
def bfs(order):
    q = deque()
    for u in range(N):
        for i in range(3):
            q.append((N-u,order[i]))

    dx = [0,-1,0]
    dy = [-1,0,1]
    kill = 0
    candi = []          # 각 궁수별 죽일 적 위치 
    check = [[0] * M for _ in range(N)]     # 현재까지 죽인 적 위치
    cnt = 0             # 현재까지 궁수 위치 수
    while q:
        x, y = q.popleft()
        visit = [[0] * M for _ in range(N)]     # 방문 체크용
        mid = deque()
        mid.append((x,y))
        flag = 0
        cnt += 1
        # 궁수별 죽일 적 최적 위치 찾기
        while mid:
            mx,my = mid.popleft()
            for k in range(3):
                a,b = mx+dx[k],my+dy[k]
                if 0<=a<N and 0<=b<M and x!=a and visit[a][b] == 0 and (abs(x-a)+abs(y-b) <= D):
                    if attacks[a][b] == 1 and check[a][b] == 0:
                        candi.append((a,b))
                        flag = 1
                        break
                    else:
                        mid.append((a,b))
                        visit[a][b] = 1
            if flag == 1:
                break
        # 한 사이클돌면 죽일 적 위치 정산
        if cnt % 3 == 0:
            while candi:
                cax,cay = candi.pop()
                if attacks[cax][cay] == 1 and check[cax][cay] == 0:
                    check[cax][cay] = 1
                    kill += 1
    return kill


N,M,D = map(int,inputs().split())
attacks = [list(map(int,inputs().split())) for _ in range(N)]
now = [0,0,0]   # 조합 초기화용
orders = []     # 조합 리스트
dfs(M,0,0)      # 조합 찾기
mini = 0        # 죽인 적 최대값 카운팅용
# 모든 조합에서 죽인 적 수 카운팅
for i in range(len(orders)):
    ans = bfs(orders[i])
    mini = max(mini,ans)

print(mini)