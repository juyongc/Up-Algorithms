from collections import deque

def solution(n, computers):
    global visit,network
    
    answer = 0
    network = computers[:]
    visit = [0]*n
    
    for i in range(n):
        # 방문한 적 없으먄 => bfs, answer ++
        if visit[i] == 0:
            bfs(i,n)
            answer += 1
    return answer

# bfs
def bfs(s,n):
    global visit,network
    
    q = deque()
    q.append(s)
    visit[s] = 1
    # 방문한 적 없고, 연결된 수면 q에 추가 / visit 체크
    while q:
        now = q.popleft()
        for k in range(n):
            if now == k:
                continue
            if visit[k] == 0 and network[now][k] == 1:
                q.append(k)
                visit[k] = 1