import heapq

def solution(n, paths, gates, summits):
    global answer
    answer = [-1,99999999999]
    tree = [[] for _ in range(n+1)]
    # 트리 만들기 node = (가중치, 연결된 노드)
    for i,j,w in paths:
        tree[i].append((w,j))
        tree[j].append((w,i))
    start = set(gates)
    destination = set(summits)
    # 모든 등산로 탐색
    for gate in gates:
        dijstra(gate,start,destination,tree,n)
    
    return answer

# 다익스트라
def dijstra(gate,start,destination,tree,n):
    global answer
    
    hq = []
    # 등산로 연결된 모든 곳 heap에 추가
    for dest in tree[gate]:
        heapq.heappush(hq,dest)
        
    visit = [0]*(n+1)
    # hq가 빌 때까지 반복
    while hq:
        val,now = heapq.heappop(hq)
        visit[now] = 1  # 현재 위치 방문체크
        # 현재값이 intensity(answer[1])보다 크다면 => return
        if val > answer[1]:
            return
        # 현재 위치가 산봉우리라면 => 상황에 따라 갱신
        if now in destination:
            if val < answer[1]:
                answer = [now,val]
            elif val == answer[1]:
                if now < answer[0]:
                    answer[0] = now
            return
        # 현재 트리와 연결된 모든 노드 탐색
        # 가중치가 크면 갱신
        # (가중치 > intensity or 이미 방문 or 등산로면) => continue
        for cost, loc in tree[now]:
            if cost > answer[1]:
                continue
            if visit[loc] or loc in start:
                continue
            heapq.heappush(hq, (max(val,cost),loc))
            
                