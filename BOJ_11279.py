import sys
import heapq
inputs = sys.stdin.readline

N = int(inputs())
hq = []
# heapq 는 최소힙 기준
# 부호 반대로 만들어서 넣기
for _ in range(N):
    num = int(inputs())
    if num:     # 0이 아니면 => 힙에 추가
        heapq.heappush(hq, -num)
    else:       # 0이면
        if hq:  # hq에 값 있으면 => 부호 반대로 출력
            now = -heapq.heappop(hq)
            print(now)
        else:   # 없으면 => 0 출력
            print(0)
