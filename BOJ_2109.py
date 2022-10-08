import sys
import heapq
inputs = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    p,d = map(int,inputs().split())
    heapq.heappush(hq,(d,p))

hq2 = []
cnt = 0
# 힙큐에서 가장 최신 날값 빼오기
# 다른 강연과 겹치지 않으면 => 강연 가기
# 겹치면 => 가장 보수 적은 날 알아보기(hq2)
#        => 현 강연보수가 더 많으면 갱신
while hq:
    day,pay = heapq.heappop(hq)
    if cnt < day:
        heapq.heappush(hq2,pay)
        cnt += 1
        continue
    min_pay = heapq.heappop(hq2)
    if pay > min_pay:
        heapq.heappush(hq2,pay)
    else:
        heapq.heappush(hq2,min_pay)

answer = 0
while hq2:
    answer += heapq.heappop(hq2)

print(answer)
