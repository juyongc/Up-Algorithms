import sys
import heapq
inputs = sys.stdin.readline

# 힙 사용해서 시작노드부터 종료노드까지 거리 찾기
# 종료노드 발견하면 리턴
def dij(s,e):

    cost = [99999999999]*(N+1)
    cost[s] = 0
    hq = [(0,s)]

    while hq:
        val,node= heapq.heappop(hq)

        if val > cost[node]:
            continue

        if node == e:
            break

        for c_node,c_val in tree[node]:
            if cost[c_node] > val + c_val:
                cost[c_node] = val + c_val
                heapq.heappush(hq,(val + c_val,c_node))
    return cost[e]


N,M = map(int,inputs().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,dist = map(int,inputs().split())
    tree[a].append((b,dist))
    tree[b].append((a,dist))

for _ in range(M):
    s,e = map(int,input().split())
    ans = dij(s,e)
    print(ans)
