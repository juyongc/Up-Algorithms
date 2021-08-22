import sys

inputs = sys.stdin.readline
N = int(inputs())
plate = [list(map(int,inputs().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]      # dp용 리스트

# 오른쪽, 아래로만 이동 가능
dx = [1,0]
dy = [0,1]
dp[0][0] = 1    # 시작점

for x in range(N):
    for y in range(N):
        if plate[x][y] != 0 and dp[x][y] != 0:  # 방문한적있고/해당 위치가 0 아니면
            for k in range(2):                  # 다음 방문지 확인
                a = x + (dx[k]*plate[x][y])
                b = y + (dy[k]*plate[x][y])
                if 0<=a<N and 0<=b<N:           # 범위 내라면
                    dp[a][b] += dp[x][y]        # 해당 위치 업데이트
ans = dp[N-1][N-1]
print(ans)