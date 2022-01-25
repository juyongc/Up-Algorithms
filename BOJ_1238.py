import sys
import heapq
inputs = sys.stdin.readline


def dij(scores, N, X):
    global maxi
    for i in range(1, N + 1):

        visit = [9999999999999] * (N + 1)
        hq = []
        visit[i] = 0
        heapq.heappush(hq, [0, i])

        while hq:
            score, city = heapq.heappop(hq)
            if visit[city] < score:
                continue

            for j in range(1, N + 1):
                cost = visit[city] + scores[city][j]
                if cost < visit[j]:
                    visit[j] = cost
                    heapq.heappush(hq, [visit[j], j])
        if i == X:
            for k in range(1,N+1):
                maxi[k] += visit[k]
        else:
            maxi[i] += visit[X]


N,M,X = map(int,inputs().split())
scores = [[9999999999999]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int,inputs().split())
    scores[s][e] = t

maxi = [0]*(N+1)
dij(scores,N, X)

print(max(maxi))
