import sys
from collections import deque
inputs = sys.stdin.readline

N,M = map(int,input().split())
object = [0]*(N+1)
cnt = [0]*(N+1)
pre = [[] for _ in range(N+1)]
# A->B: A 선이수 필수
for _ in range(M):
    A,B = map(int,inputs().split())
    pre[A].append(B)
    cnt[B] += 1

q = deque()
# 초기값 정하기
for i in range(1,N+1):
    if cnt[i] == 0:
        q.append((i,1))

while q:
    now,val = q.popleft()
    object[now] = val
    for num in pre[now]:
        cnt[num] -= 1
        if cnt[num] == 0:   # 선이수 다 이수했으면 => 큐에 추가
            q.append((num,val+1))

print(" ".join(map(str,object[1:])))
