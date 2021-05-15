import sys
from collections import deque


def move():
    global ans
    # 큐 돌리기
    while q:
        # x,y,horse,tot: 현재 x,y 좌표, 말처럼 이동 횟수, 총 이동 횟수
        x,y,horse,tot = q.popleft()
        # 정답이면 리턴
        if x == H-1 and y == W-1:
            ans = tot
            return
        # 말처럼 이동이 남았다면,
        if horse < K:
            for k in range(8):
                a,b = x+dx1[k],y+dy1[k]
                if a == H - 1 and b == W - 1:   # 정답이면 리턴
                    ans = tot+1
                    return
                # 범위 내 / 이동가능한 위치 / 방문체크
                # *** horse+1인 이유: 그냥 horse가 이동하면 해당 위치로 이동 시 horse+1 돼서 중복됨
                if 0<=a<H and 0<=b<W and road[a][b] == 0:
                    if visit[a][b] == -1 or visit[a][b] > horse+1:
                        q.append((a,b,horse+1,tot+1))
                        visit[a][b] = horse+1       # *** horse+1인 이유: 그냥 horse면 원숭이 이동이라 판별 불가
        # 상하좌우 이동
        for k in range(4):
            a,b = x+dx2[k],y+dy2[k]
            if a == H - 1 and b == W - 1:
                ans = tot+1
                return
            if 0<=a<H and 0<=b<W and road[a][b] == 0:
                if visit[a][b] == -1 or visit[a][b] > horse:
                    q.append((a,b,horse,tot+1))
                    visit[a][b] = horse

inputs = sys.stdin.readline
K = int(input())
W,H = map(int,inputs().split())
road = [list(map(int,inputs().split())) for _ in range(H)]
visit = [[-1]*W for _ in range(H)]
# 나이트 이동
dx1 = [2,2,1,1,-2,-2,-1,-1]
dy1 = [1,-1,2,-2,1,-1,2,-2]
# 상하좌우 이동
dx2 = [1,-1,0,0]
dy2 = [0,0,1,-1]

q = deque()
# x좌표, y좌표, 말처럼 움직인 횟수, 전체 이동 횟수
q.append((0,0,0,0))
visit[0][0] = 0     # 출발지 방문 체크
ans = -1            # ans 디폴트: -1
move()
print(ans)