import sys
import heapq
inputs = sys.stdin.readline

V,E = map(int,inputs().split())
K = int(inputs().rstrip())
nodes = {}
# 최소값만 가진 노드 딕셔너리 만들기
for _ in range(E):
    u,v,w = map(int,inputs().split())
    if u in nodes:
        if v in nodes[u]:
            nodes[u][v] = min(w,nodes[u][v])
        else:
            nodes[u][v] = w
    else:
        nodes[u] = {v:w}

# 다익스트라
q = []
heapq.heappush(q,(0,K))
vals = [9999999999]*(V+1)
vals[0] = 0
vals[K] = 0
while q:
    cost,now = heapq.heappop(q)
    if cost > vals[now]:    # 이미 갱신됐으면 => 넘기기
        continue

    if now in nodes:
        for daum in nodes[now].keys():
            if vals[daum] > (vals[now]+nodes[now][daum]):
                vals[daum] = vals[now]+nodes[now][daum]
                heapq.heappush(q,(vals[daum],daum))

for i in range(1,V+1):
    if vals[i] == 9999999999:
        print("INF")
    else:
        print(vals[i])
