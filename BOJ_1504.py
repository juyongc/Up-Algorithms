import sys
import heapq
inputs = sys.stdin.readline

# 다익스트라
def dijk(s,e):

    W = [99999999999999]*(N+1)
    W[s] = 0
    hq = []
    heapq.heappush(hq,(W[s],s))
    
    while hq:
        cost, idx = heapq.heappop(hq)
        if idx == e:    # 도착점 도달
            return W[e]
        # 모든 노드 거리에서 최단거리 있으면 갱신 및 hq에 추가
        for k in range(1,N+1):
            if nodes[idx][k] > 0:
                if W[idx]+nodes[idx][k] < W[k]:
                    W[k] = W[idx]+nodes[idx][k]
                    heapq.heappush(hq,(W[k],k))
    return W[e]


N,M = map(int,inputs().split())
nodes = [[0]*(N+1) for _ in range(N+1)]
# 노드 양방향 거리 리스트
for _ in range(M):
    a,b,c = map(int,inputs().split())
    nodes[a][b] = c
    nodes[b][a] = c
v1,v2 = map(int,inputs().split())

route1 = dijk(1,v1) + dijk(v1,v2) + dijk(v2,N)  # 1 -> v1 -> v2 -> N
route2 = dijk(1,v2) + dijk(v2,v1) + dijk(v1,N)  # 1 -> v2 -> v1 -> N

mini = min(route1,route2)
if mini >= 99999999999999:      # 가능한 경로 미존재
    mini = -1

print(mini)