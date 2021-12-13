import sys
inputs = sys.stdin.readline

N = int(input())
M = int(input())
W = [[999999999999999]*N for _ in range(N)]
# 가중치 세팅
for _ in range(M):
    a,b,c = map(int,inputs().split())
    W[a-1][b-1] = min(W[a-1][b-1],c)

# 플로이드 와샬
for k in range(N):          # 중간 지점
    W[k][k] = 0
    for i in range(N):      # 시작 지점
        for j in range(N):  # 종료 지점
            if i == j:
                continue
            W[i][j] = min(W[i][j],W[i][k]+W[k][j])

# 못 가는 곳 => 0으로 변경
for i in range(N):
    for j in range(N):
        if W[i][j] == 999999999999999:
            W[i][j] = 0

# 출력
for i in range(N):
    print(' '.join(map(str,W[i])))