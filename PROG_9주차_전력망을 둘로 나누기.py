from collections import deque
def solution(n, wires):
    answer = 99999999999
    
    # 트리 확인하기
    def istree(x,y):
        visit = [0]*(n+1)
        q = deque()
        q.append(x)
        visit[x] = 1
        # 방문 체크
        while q:
            now = q.popleft()
            for i in range(1,n+1):
                if nodes[now][i] == 1 and visit[i] == 0:
                    if i == y:
                        return -1
                    visit[i] = 1
                    q.append(i)
        one = 0
        zero = 0
        # 0,1 확인하기
        for j in range(1,n+1):
            if visit[j] == 1:
                one += 1
            else:
                zero += 1
        return abs(one - zero)

    nodes = [[0]*(n+1) for _ in range(n+1)]
    # 트리 만들기
    for wire in wires:
        v1,v2 = wire[0],wire[1]
        nodes[v1][v2] = 1
        nodes[v2][v1] = 1
        
    # 연결 끊기 & 확인하기
    for wire in wires:
        v1,v2 = wire[0],wire[1]
        nodes[v1][v2] = 0
        nodes[v1][v2] = 0
        ans = istree(v1,v2)
        if ans >= 0:
            answer = min(answer,ans) 
        nodes[v1][v2] = 1
        nodes[v2][v1] = 1
        
    return answer