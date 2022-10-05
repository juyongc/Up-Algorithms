import sys
import heapq
inputs = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    d,w = map(int,inputs().split())
    heapq.heappush(hq,(-w,d))   # 힙큐 - 최소값 뽑아냄 => 점수 마이너스로 넣기

visit = [0]*(N+1)

cnt = 0
# 전부 채워졌으면 최대값임
while cnt < N:
    if not hq:      # 모든 과제 체크한 상태라서 break
        break
    score, deadline = heapq.heappop(hq)
    if deadline > N:    # 마감일 최대는 N
        deadline = N
    # 마감일부터 내려오면서 가능한 날짜에 과제하기
    # 과제하면 방문체크 및 cnt ++
    for i in range(deadline,0,-1):
        if visit[i]:
            continue
        visit[i] = -score
        cnt += 1
        break

print(sum(visit))
