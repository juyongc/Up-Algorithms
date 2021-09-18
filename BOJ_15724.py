import sys
inputs = sys.stdin.readline
N,M = map(int,inputs().split())
land = [list(map(int,inputs().split())) for _ in range(N)]
prefix = [[0]*(M+1) for _ in range(N+1)]
# 위치별 누적합 구하기
for i in range(1,N+1):
    for j in range(1,M+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + land[i-1][j-1]
K = int(inputs())
# 누적합에서 불필요한 부분 빼고 중복된 부분 합하기
for _ in range(K):
    x1,y1,x2,y2 = map(int,inputs().split())
    ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(ans)