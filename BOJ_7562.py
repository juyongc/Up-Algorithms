import sys
from collections import  deque

# BFS
def bfs():
    q = deque()
    q.append((now))
    plate[now[0]][now[1]] = 0   # 최초 위치 -> 0
    while q:
        x,y = q.popleft()
        # 8방향 탐색
        for k in range(8):
            a,b = x+dx[k],y+dy[k]
            # 체스판 내에서 미방문이라면,
            if 0<=a<L and 0<=b<L and plate[a][b] == -1:
                plate[a][b] = plate[x][y] + 1   # 방문할 위치 = 현 위치 + 1
                # 목표 위치 -> return / 아니면 append
                if a == goal[0] and b == goal[1]:
                    return plate[a][b]
                else:
                    q.append([a,b])


inputs = sys.stdin.readline
T = int(inputs())           # 테스트 케이스 수
for t in range(1,T+1):
    L = int(inputs())       # 체스판 크기
    now = list(map(int,inputs().split()))   # 현 위치
    goal = list(map(int,inputs().split()))  # 목표 위치
    plate = list([-1]*L for _ in range(L))  # 판 만들기 -> 방문 체크용
    # 8방향
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    # 현 위치랑 목표 위치가 같으면
    if now == goal:
        ans = 0
    else:
        ans = bfs()

    print(ans)