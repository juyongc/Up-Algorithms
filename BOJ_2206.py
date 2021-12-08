import sys
from collections import deque
inputs = sys.stdin.readline

# BFS 탐색
def bfs():

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 0 => 이전까지 부순적 없음 / 1 => 이미 한번 부쉈음
    visit = [[[99999999999,99999999999] for _ in range(M)] for _ in range(N)]

    visit[0][0][0] = 1
    q = deque()
    q.append((0,0,0,1))   # x좌표, y좌표, 벽 부쉈는지 체크(0:X, 1:O),경로 횟수

    while q:
        x,y,smash,cnt = q.popleft()
        # 해당 위치 최소값이 이미 갱신됐으면 => continue
        if cnt > visit[x][y][smash]:
            continue
        # 4방향 탐색
        for k in range(4):
            a, b = x + dx[k], y + dy[k]
            if 0 <= a < N and 0 <= b < M:
                # 벽을 만났고, 부수고 지나간다면
                if board[a][b] == '1' and smash == 0:
                    if cnt + 1 < visit[a][b][1]:
                        visit[a][b][1] = cnt + 1
                        q.append((a,b,1,cnt+1))
                # 벽이 아니라면
                elif board[a][b] == '0':
                    if cnt + 1 < visit[a][b][smash]:
                        visit[a][b][smash] = cnt + 1
                        q.append((a, b, smash, cnt + 1))
    # 도착지에서 최소값 찾기
    ans = min(visit[N-1][M-1][0],visit[N-1][M-1][1])
    if ans == 99999999999:
        ans = -1
    return ans

N,M = map(int,inputs().split())
board = [list(inputs().rstrip()) for _ in range(N)]

answer = bfs()

print(answer)
