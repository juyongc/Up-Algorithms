import sys
from collections import deque
inputs = sys.stdin.readline

# 회전
def rot(r, c, s):
    global arr
    sr, sc = r - s - 1, c - s - 1
    er, ec = r + s - 1, c + s - 1
    while sr < er:
        q = deque()
        for i in range(sc, ec):
            q.append(arr[sr][i])
        for i in range(sr, er):
            q.append(arr[i][ec])
        for i in range(ec, sc, -1):
            q.append(arr[er][i])
        for i in range(er, sr, -1):
            q.append(arr[i][sc])
        q.rotate(1)
        for i in range(sc, ec):
            arr[sr][i] = q.popleft()
        for i in range(sr, er):
            arr[i][ec] = q.popleft()
        for i in range(ec, sc, -1):
            arr[er][i] = q.popleft()
        for i in range(er, sr, -1):
            arr[i][sc] = q.popleft()

        sr += 1
        sc += 1
        er -= 1
        ec -= 1

# 역방향 회전(원상태로 만들기 위해)
def rot_reverse(r, c, s):
    sr, sc = r - s - 1, c - s - 1
    er, ec = r + s - 1, c + s - 1
    while sr < er:
        q = deque()
        for i in range(sc, ec):
            q.append(arr[sr][i])
        for i in range(sr, er):
            q.append(arr[i][ec])
        for i in range(ec, sc, -1):
            q.append(arr[er][i])
        for i in range(er, sr, -1):
            q.append(arr[i][sc])
        q.rotate(-1)
        for i in range(sc, ec):
            arr[sr][i] = q.popleft()
        for i in range(sr, er):
            arr[i][ec] = q.popleft()
        for i in range(ec, sc, -1):
            arr[er][i] = q.popleft()
        for i in range(er, sr, -1):
            arr[i][sc] = q.popleft()

        sr += 1
        sc += 1
        er -= 1
        ec -= 1

# 순서 정하기
def dfs(cnt):
    global mini, visit, arr, area

    if cnt >= K:
        for i in range(N):
            mini = min(mini, sum(arr[i]))
        return

    for j in range(K):
        if visit[j] == 1:
            continue
        visit[j] = 1
        rot(area[j][0], area[j][1], area[j][2])
        dfs(cnt + 1)
        rot_reverse(area[j][0], area[j][1], area[j][2])
        visit[j] = 0

N,M,K = map(int,inputs().split())
arr = [list(map(int,inputs().split())) for _ in range(N)]
area = [list(map(int,inputs().split())) for _ in range(K)]
visit = [0]*K
mini = 99999999999
dfs(0)
print(mini)
