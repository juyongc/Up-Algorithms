import sys
inputs = sys.stdin.readline


def dfs(s, now, cnt, money):
    global mini
    if money >= mini:   # 최소값을 넘었으면 => return
        return

    if cnt == N - 1:
        if trips[now][s] != 0:      # 시작점 복귀
            money += trips[now][s]
            mini = min(mini, money)
        return
    else:
        # 다음 방문할 곳이 조건에 맞다면 dfs 이동
        for i in range(N):  
            if trips[now][i] != 0 and visit[i] == 0:
                visit[i] = 1
                dfs(s, i, cnt + 1, money + trips[now][i])
                visit[i] = 0


N = int(inputs())
trips = [list(map(int,inputs().split())) for _ in range(N)]

mini = 99999999999
visit = [0]*N
costs = [0]*N

# 모든 위치 dfs 시작하기
for k in range(N):
    visit[k] = 1
    dfs(k,k,0,0)
    visit[k] = 0

print(mini)