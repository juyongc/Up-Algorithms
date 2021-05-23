import sys
import heapq


def mst(s):
    tot = 0
    visit = [0] * (V + 1)
    hq = []
    heapq.heappush(hq, (0 ,1))      # (가중치, node 번호)
    while hq:
        now = heapq.heappop(hq)
        if visit[now[1]] != 0:
            continue
        visit[now[1]] = 1

        tot += now[0]
        for node in W[now[1]]:
            if visit[node[0]] == 0:
                heapq.heappush(hq, (node[1], node[0]))
    return tot


inputs = sys.stdin.readline
V,E = map(int,inputs().split())

W = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,inputs().split())
    W[a].append((b,c))
    W[b].append((a,c))

ans = mst(1)
print(ans)