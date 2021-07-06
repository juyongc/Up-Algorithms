import sys

inputs = sys.stdin.readline
N,M = map(int,inputs().split())

# 앞에 0인 리스트를 더해줌
table = [[0]*(N+1)]+[[0]+list(map(int,inputs().split())) for _ in range(N)]

# 0,0 부터 x2,y2까지 각각의 합 계산
for i in range(1,N+1):
    for j in range(N+1):
        table[i][j] += table[i-1][j]
for j in range(1,N+1):
    for i in range(N+1):
        table[i][j] += table[i][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,inputs().split())
    # (x1,y1)~(x2,y2) = (x2,y2) - (x2,y1-1) - (x1-1,y2) + (x1-1,y1-1)
    ans = table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]
    print(ans)