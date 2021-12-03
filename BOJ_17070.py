import sys
inputs = sys.stdin.readline

N = int(input())
walls = [list(map(int,inputs().split())) for _ in range(N)]
# 0 - 가로/ 1 - 대각선 / 2 - 세로
pipe = [list([0]*3 for _ in range(N)) for _ in range(N)]
pipe[0][1][0] = 1   # 시작점

for x in range(N):
    for y in range(N):
        if x == N-1 and y == N-1:   # 끝남
            continue
        if walls[x][y] == 1:        # 못지나가는 공간
            continue
        for k in range(3):
            if pipe[x][y][k] == 0:  # 파이프 없음
                continue
            else:                   # 파이프가 있으면
                if k == 0:      # 가로
                    if y < N - 1 and walls[x][y + 1] == 0:
                        pipe[x][y+1][0] += pipe[x][y][0]
                    if y<N-1 and x<N-1 and walls[x][y+1] == 0 and walls[x+1][y] == 0 and walls[x+1][y+1] == 0:
                        pipe[x+1][y+1][1] += pipe[x][y][0]
                elif k == 1:    # 대각선
                    if y<N-1 and walls[x][y+1] == 0:
                        pipe[x][y + 1][0] += pipe[x][y][1]
                    if y<N-1 and x<N-1 and walls[x][y+1] == 0 and walls[x+1][y] == 0 and walls[x+1][y+1] == 0:
                        pipe[x + 1][y + 1][1] += pipe[x][y][1]
                    if x<N-1 and walls[x+1][y] == 0:
                        pipe[x + 1][y][2] += pipe[x][y][1]
                else:           # 세로
                    if y<N-1 and x<N-1 and walls[x][y+1] == 0 and walls[x+1][y] == 0 and walls[x+1][y+1] == 0:
                        pipe[x + 1][y + 1][1] += pipe[x][y][2]
                    if x<N-1 and walls[x+1][y] == 0:
                        pipe[x + 1][y][2] += pipe[x][y][2]

ans = sum(pipe[N-1][N-1])

print(ans)