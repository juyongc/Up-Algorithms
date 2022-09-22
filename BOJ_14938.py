import sys
import heapq
inputs = sys.stdin.readline

# 다익스트라
def dij(N, start, route):
    W = [999999999] * (N + 1)   # 수색 범위값 리스트
    W[start] = 0

    hq = [(0, start)]   # 시작점 초기화 (value, 시작점)

    while hq:
        val, loc = heapq.heappop(hq)
        if val > W[loc]:        # 최신 업데이트된 값 아니면 continue
            continue
        # 현재 시작점의 모든 수색 가능한 지점 탐색
        for k in range(len(route[loc])):
            next_val, next_loc = route[loc][k]
            # W[다음 지점] > 현재 지점 수색 값 + 다음 지점 수색 값 => 갱신 가능
            if val + next_val < W[next_loc]:
                W[next_loc] = val + next_val
                heapq.heappush(hq, (W[next_loc], next_loc))
    return W


N,M,R = map(int,inputs().split())
item_num = [0] + list(map(int,inputs().split()))
route = [[] for _ in range(N+1)]

for _ in range(R):
    a,b,l = map(int,inputs().split())
    route[a].append((l,b))
    route[b].append((l,a))

maxi = 0
# 모든 지점 수색하기
for i in range(1,N+1):
    search_list = dij(N,i,route)
    item = 0
    # 수색 범위 내면 아이템 개수 카운팅
    for j in range(1,N+1):
        if search_list[j] <= M:
            item += item_num[j]
    maxi = max(maxi,item)

print(maxi)