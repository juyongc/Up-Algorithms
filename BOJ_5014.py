import sys
from collections import deque

# BFS 탐색
def bfs():
    q = deque()
    q.append((S,0))     # (시작위치, 버튼 누른 횟수)
    visit = [0]*(F+1)   # 방문 체크용
    visit[S] = 1
    # 큐 반복
    while q:
        now,cnt = q.popleft()
        up = now + U        # U만큼 위로
        down = now - D      # D만큼 아래로
        cnt += 1            # 버튼 누른 횟수 ++
        
        if 0 < up <= F and visit[up] == 0:  # 위로 갔을 때,
            if up == G:                     # 도착
                ans = cnt                   # 정답
                return ans
            else:                           # 도착지 아니면
                visit[up] = 1               # 방문체크
                q.append((up,cnt))          # 큐에 추가
        if 0 < down <= F and visit[down] == 0:  # 아래로 갔을 때,
            if down == G:                       # 도착
                ans = cnt                       # 정답
                return ans
            else:                               # 도착지 아니면
                visit[down] = 1                 # 방문체크
                q.append((down,cnt))            # 큐에 추가
    
    return "use the stairs"         # 갈 수 있는 방법이 없음 -> 출력


inputs = sys.stdin.readline
F,S,G,U,D = map(int,inputs().split())

if S == G:
    print(0)
else:
    final = bfs()
    print(final)