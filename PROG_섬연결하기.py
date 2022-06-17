import heapq

def dij(s,n,w):
    visit = [0]*n
    mini = [9999999999]*n
    hq = []
    mini[s] = 0
    heapq.heappush(hq,(mini[s],s))
    # 현재 노드 방문처리
    # 방문 가능한 미방문지와 값 비교 후, 최소값이면 갱신
    while hq:
        val,now = heapq.heappop(hq)
        visit[now] = 1
        if val > mini[now]:
            continue
        for i in range(n):
            if w[i] == 0 or visit[i] == 1:
                continue
            if w[now][i] < mini[i]:
                mini[i] = w[now][i]
                heapq.heappush(hq,(mini[i],i))
    return sum(mini)


def solution(n, costs):
    answer = 0
    w = [[99999999999]*n for _ in range(n)]
    for cost in costs:
        s,e,c = cost
        w[s][e] = c
        w[e][s] = c
    answer = dij(0,n,w)
    return answer