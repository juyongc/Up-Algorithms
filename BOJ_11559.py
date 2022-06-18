import sys
from collections import deque
import heapq
inputs = sys.stdin.readline

# 버블 4개 이상 확인하기
def bfs(x, y):
    bubble = [(x, y)]           # 버블 개수 및 위치 확인용
    visit[x][y] = 1

    bubble_q = deque()          # 현재 검사중인 버블들
    bubble_q.append((x, y))
    while bubble_q:
        r, c = bubble_q.popleft()
        for k in range(4):
            rr, cc = r + dx[k], c + dy[k]
            if 0 <= rr < 12 and 0 <= cc < 6 and visit[rr][cc] == 0:
                if puyo[rr][cc] == puyo[r][c]:
                    bubble_q.append((rr, cc))
                    bubble.append((rr, cc))
                    visit[r][c] = 1

    # 4개 이상이면 터뜨리고, 1 반환
    if len(bubble) >= 4:
        for a, b in bubble:
            puyo[a][b] = "."
        return 1

    return 0

# 위에 있는 뿌요들 바닥으로 내리기
def down():

    for i in range(6):
        zero = []       # 빈칸인 곳
        for j in range(11, -1, -1):
            if puyo[j][i] == ".":               # 빈칸이면 zero에 추가
                heapq.heappush(zero,-j)
            else:
                if zero:                        # zero가 있으면
                    zx = heapq.heappop(zero)    # zero에서 꺼내고 자리바꿈
                    puyo[-zx][i] = puyo[j][i]   # 뿌요있던 위치는 빈칸으로
                    puyo[j][i] = "."            # zero에 현 위치 추가
                    heapq.heappush(zero,-j)


puyo = [list(input()) for _ in range(12)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

flag = 0
total = 0

# 갱신된 적 없으면 중단
while flag == 0:

    q = deque()
    # 뿌요인 부분 찾기
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != ".":
                q.append((i,j))

    visit = [[0]*6 for _ in range(12)]      # 뿌요 위치 방문 체크용
    cnt = 0                                 # 갱신 체크용
    # 모든 뿌요 검사하기
    while q:
        x,y = q.popleft()
        if puyo[x][y] == ".":
            continue
        if visit[x][y] == 1:
            continue

        check = bfs(x,y)
        if check == 1:
            cnt = 1

    total += cnt
    # 갱신 기록 없으면 => 중단
    # 갱신 기록 있으면 => 내리기
    if cnt == 0:
        flag = 1
        break
    else:
        down()

print(total)
