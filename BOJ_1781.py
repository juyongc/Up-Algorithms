import sys
import heapq
inputs = sys.stdin.readline

N = int(input())
given = [list(map(int,inputs().split())) for _ in range(N)]
given.sort()    # 데드라인에 맞게 정렬

hq = []
# 힙에 추가하면서 데드라인보다 많아지면 => 작은 값 빼내기
for deadline,num in given:
    heapq.heappush(hq,num)
    if len(hq) > deadline:
        heapq.heappop(hq)

answer = 0
# 정답 계산
for val in hq:
    answer += val

print(answer)
