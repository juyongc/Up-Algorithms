import sys
import heapq
inputs = sys.stdin.readline

# 다익스트라
def find_short(n):
    W = [10 ** 10] * (N + 1)
    hq = []

    W[1], W[n] = 0, 0
    heapq.heappush(hq,(0, 1))
    while hq:
        cost, now = heapq.heappop(hq)

        if cost > W[now]:
            continue

        if now == N:
            return cost

        for dest, val in road[now]:
            if W[dest] > cost + val:
                W[dest] = cost + val
                heapq.heappush(hq, (cost + val, dest))
    return -1


N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,inputs().split())
    road[a].append((b,t))
    road[b].append((a,t))

standard = find_short(1)    # 미검문 최단거리
answer = 0
# 각 i지점 검문 시, 최단거리
for i in range(2,N):
    block = find_short(i)
    if block == -1:     # -1이 나오면 끝
        answer = -1
        break
    else:               # 가장 오래걸리는지 확인
        answer = max(answer,block - standard)

print(answer)

