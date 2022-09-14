import sys
from collections import deque
inputs = sys.stdin.readline

n,m = map(int,inputs().split())
superior = [0] + list(map(int,inputs().split()))    # 직속상사 리스트
W = [0]*len(superior)                               # 칭찬량 

# 직속상사한테 받은 칭찬량 계산
for _ in range(m):
    worker, amount = map(int,inputs().split())
    W[worker] += amount

underling = [[] for _ in range(len(superior))]      # 부하직원 리스트
for i in range(2,len(superior)):
    underling[superior[i]].append(i)

# 자신의 칭찬량을 부하직원한테 더하기
q = deque([1])
while q:
    now = q.popleft()
    for under in underling[now]:
        W[under] += W[now]
        q.append(under)

print(" ".join(map(str,W[1:])))
