import sys
inputs = sys.stdin.readline

# 벨만 포드
def bellman(s):

    cost[s] = 0

    for i in range(N):
        for j in range(M):
            x,y,val = dists[j]
            if cost[x] != 999999999999 and cost[x]+val < cost[y]:
                cost[y] = cost[x]+val
                if i == N-1:    # 음수 사이클 체크
                    return -1
    return 1


N,M = map(int,inputs().split())
dists = []
cost = [999999999999]*(N+1)
for _ in range(M):
    a,b,c = map(int,inputs().split())
    dists.append((a,b,c))

check = bellman(1)

if check == -1:
    print(-1)
else:
    for k in range(2,N+1):
        if cost[k] == 999999999999:
            print(-1)
        else:
            print(cost[k])