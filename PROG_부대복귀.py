import heapq
def solution(n, roads, sources, destination):
    answer = []
    route = [[] for _ in range(n+1)]
    for a,b in roads:
        route[a].append(b)
        route[b].append(a)
    
    ans = dij(destination,route)
    for source in sources:
        if ans[source] == 9999999999:
            answer.append(-1)
        else:
            answer.append(ans[source])
    
    return answer

# 다익스트라 - 목적지에서 부대원 위치까지 최단거리 구하기
def dij(destination,route):
    
    hq = []
    heapq.heappush(hq,(0,destination))
    W = [9999999999]*len(route)
    W[destination] = 0
    
    while hq:
        val,node = heapq.heappop(hq)
        if val > W[node]:
            continue
        
        for no in route[node]:
            next_val = val + 1
            if next_val < W[no]:
                W[no] = next_val
                heapq.heappush(hq,(next_val,no))
        
    return W