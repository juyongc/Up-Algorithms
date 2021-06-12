import sys

inputs = sys.stdin.readline

N,S,M = map(int,inputs().split())
V = list(map(int,inputs().split()))
# dp: 가능한 모든 볼륨
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1
# 해당 볼륨 가능하면 => 1
for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j] == 1:
            now = j
            now1 = now + V[i-1]
            now2 = now - V[i-1]
            if now1 <= M:
                dp[i][now1] = 1
            if 0<= now2:
                dp[i][now2] = 1

ans = -1    # 정답 디폴트
# 가장 큰 값부터 내려가면서 답 나오면 break
for i in range(M,-1,-1):
    if dp[-1][i] == 1:
        ans = i
        break

print(ans)