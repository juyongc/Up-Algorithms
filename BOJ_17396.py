import sys
import heapq
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
discover = list(map(int,inputs().split()))
discover[-1] = 0
road = [{} for _ in range(N)]       # 길 저장용
for _ in range(M):
    a,b,t = map(int,inputs().split())
    road[a][b] = t
    road[b][a] = t

weight = [10**15] * N
hq = []
heapq.heappush(hq,(0,0))
# 최소 시간 찾기(다익스트라)
while hq:
    w,node = heapq.heappop(hq)
    if w > weight[node]:
        continue

    for key,val in road[node].items():
        if weight[key] > w + val and discover[node] == 0:
            weight[key] = w + val
            heapq.heappush(hq,(w + val,key))

answer = weight[-1]
if answer == 10**15:
    answer = -1
print(answer)