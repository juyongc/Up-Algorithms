import sys
inputs = sys.stdin.readline

# BFS 탐색
def bfs(num):
    visit = [[0] * N for _ in range(N)]
    # 잠긴 지역 표시
    for r in range(N):
        for c in range(N):
            if rains[r][c] <= num:
                visit[r][c] = -1

    s = []
    # 안잠긴 지역 리스트에 추가
    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0:
                s.append((x, y))

    cnt = 1
    
    if len(s) <= ans:   # max 비교할 필요없으면 넘기기
        return 0
    else:               # 안전지역 합치기
        for val in s:
            x1, y1 = val[0], val[1]
            if visit[x1][y1] == 0:
                stack = [(x1, y1)]
            else:
                continue

            visit[x1][y1] = cnt 
            while stack:    # 같은 안전지역 카운팅용
                x2, y2 = stack.pop()
                for k in range(4):
                    a = x2 + dx[k]
                    b = y2 + dy[k]
                    if 0 <= a < N and 0 <= b < N and visit[a][b] == 0:
                        visit[a][b] = cnt
                        stack.append((a, b))
            cnt += 1
        return cnt-1


N = int(inputs())
rains = [list(map(int,inputs().split())) for _ in range(N)]
maxi = 0
mini = 1000
# 비교할 필요 있는 구간 찾기(min,max)
for i in range(N):
    for j in range(N):
        maxi = max(maxi,rains[i][j])
        mini = min(mini,rains[i][j])
ans = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(mini,maxi):
    now = bfs(i)
    ans = max(ans,now)

print(ans)
