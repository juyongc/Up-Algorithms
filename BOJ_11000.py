import sys
import heapq
inputs = sys.stdin.readline

N = int(inputs().rstrip())
classTime = []
# 전체 수강시간 리스트로 만들기
for _ in range(N):
    s,e = map(int,inputs().split())
    classTime.append((s,e))

classTime.sort()
hq = []
# 우선순위 큐로 시간별로 변경하기
for curTime in classTime:
    if hq and hq[0] <= curTime[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,curTime[1])

print(len(hq))