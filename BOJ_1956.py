import sys
import heapq
inputs = sys.stdin.readline

def find_path(road):

    cost = [[99999999]*len(road) for _ in range(len(road))]
    hq = []
    for i in range(1,len(road)):
        heapq.heappush(hq,(0,i,0))

    while hq:
        value,now,prev = heapq.heappop(hq)      # 현재값, 현재 노드, 이전 노드

        if now == prev:
            return value
        # prev == 0인 첫 시작이면, 시작점으로 정정해주기
        if prev == 0:
            prev = now
        # 이미 갱신된 값이면 넘기기
        if cost[prev][now] < value:
            continue
        # 현재 -> 다음 값, 다음 노드
        # 시작노드 ~ 다음 노드까지의 거리 계산 후, 기존과 비교
        for r_cost,r_point in road[now]:
            current = value + r_cost
            if current > cost[prev][r_point]:
                continue
            cost[prev][r_point] = current
            heapq.heappush(hq, (current, r_point, prev))

    return 999999999


N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append((c,b))
mini = 999999999

ans = find_path(road)
mini = min(ans,mini)

if mini == 999999999:
    mini = -1
print(mini)