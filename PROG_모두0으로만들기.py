from collections import deque
# 한 노드를 최상위 노드로 찍고 이하 자식 노드들 찾기
def find_level(nodes):
    visit = [0]*len(nodes)
    q = deque()     # 방문할 노드
    stack = []      # 연결된 부모-자식 노드
    q.append(0)
    visit[0] = 1
    while q:
        now = q.popleft()
        for node in nodes[now]:
            if visit[node] == 0:
                q.append(node)
                stack.append((now,node))
                visit[node] = 1
    
    return stack
            
    
def solution(a, edges):
    answer = 0
    nodes = [[] for _ in range(len(a))]
    # 각 노드별 연결된 노드 구하기 
    for u,v in edges:
        nodes[u].append(v)
        nodes[v].append(u)

    order = find_level(nodes)
    cnt = 0
    # 찾은 부모-자식 노드에서 자식에서 부모로 값 옮기기
    # 음수값도 있으니 abs로 양수값으로 만들어서 더하기
    while order:
        u,v = order.pop()
        a[u] += a[v]
        cnt += abs(a[v])
        a[v] = 0
    answer = cnt
    # 불가능한 경우 찾기
    for zero in a:
        if zero != 0:
            answer = -1
            break
    return answer