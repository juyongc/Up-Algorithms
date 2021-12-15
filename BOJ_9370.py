import sys
import heapq
inputs = sys.stdin.readline

# 다익스트라
def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    tot = [999999999999] * (n + 1)
    tot[start] = 0

    while hq:
        distance, node = heapq.heappop(hq)

        for i in range(1, n + 1):
            new_distance = distance + W[node][i]
            if new_distance < tot[i]:
                tot[i] = new_distance
                heapq.heappush(hq, (new_distance, i))
    return tot  # 시작점부터 인덱스별 최단거리 값 리스트


T = int(input())
for _ in range(T):
    n,m,t = map(int,inputs().split())
    s,g,h = map(int,inputs().split())
    W = [[999999999999]*(n+1) for _ in range(n+1)]
    for _ in range(m):
       a,b,d = map(int,inputs().split())
       W[a][b] = d
       W[b][a] = d
    destinations = [int(input()) for _ in range(t)]

    StoGH = dijkstra(s)     # 시작점부터 모든 노드
    GtoD = dijkstra(g)      # g ~ 모든 노드
    HtoD = dijkstra(h)      # h ~ 모든 노드
    ans = []

    # 모든 후보지 확인
    for destination in destinations:
        absolute = StoGH[destination]   # 시작점 ~ 후보지 최단거리
        # g~h 교차로 이용 여부 탐색
        # s~g~h~후보지 vs s~h~g~후보지 사이에서 최단거리 확인 
        find_min = min(StoGH[g]+HtoD[destination],StoGH[h]+GtoD[destination]) + W[g][h]
        if absolute == find_min:    # absolute 와 find_min 같은 지 확인 => 같으면 append
            ans.append(destination)

    ans.sort()
    print(' '.join(map(str,ans)))