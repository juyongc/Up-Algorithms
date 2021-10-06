import sys
inputs = sys.stdin.readline

N = int(inputs().rstrip())
costs = [list(map(int,inputs().split())) for _ in range(N)]
# 똑같은 인덱스 제외하고 min값 구하기
for i in range(1,N):
    for j in range(3):
        costs[i][j] += min(costs[i-1][:j]+costs[i-1][j+1:])

print(min(costs[-1]))