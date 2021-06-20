import sys
import heapq

def mst(s):
    tot = 0
    visit = [0]*(N+1)
    hq = []
    heapq.heappush(hq,(0,1))

    while hq:
        now = heapq.heappop(hq)
        if visit[now[1]] != 0:
            continue
        visit[now[1]] = 1

        tot += now[0]
        for node in trees[now[1]]:
            if visit[node[0]] == 0:
                heapq.heappush(hq,(node[1],node[0]))

    return tot


inputs = sys.stdin.readline
N = int(inputs())
M = int(inputs())
trees = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,inputs().split())
    if a == b:
        trees[a].append((b,c))
    else:
        trees[a].append((b,c))
        trees[b].append((a,c))

if N == 1:
    trees[1].sort(key=lambda x: x[1])
    ans = trees[1][0][1]
else:
    ans = mst(1)

# print(trees)
print(ans)
