import sys

inputs = sys.stdin.readline
T = int(inputs())
for t in range(1,T+1):
    N,M = map(int,inputs().split())
    for _ in range(M):
        a,b = map(int,inputs().split())
    # 연결그래프 => 모든 정점 연결되어있음
    print(N-1)