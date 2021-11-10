import sys
import heapq
inputs = sys.stdin.readline

N = int(input())

hq = []
for _ in range(N):
    tables = list(map(int,inputs().split()))
    if not hq:      # hq가 비었으면 => 현재 테이블값 다 넣기
        for table in tables:
            heapq.heappush(hq,table)

    else:           # hq에 값이 있으면 => hq[0]보다 큰 값 나오면 변경
        for table in tables:
            now = hq[0]
            if table > now:
                heapq.heappop(hq)
                heapq.heappush(hq,table)

print(hq[0])
