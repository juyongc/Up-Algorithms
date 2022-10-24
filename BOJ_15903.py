import sys
import heapq
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
nums = list(map(int,inputs().split()))

hq = []
for num in nums:
    heapq.heappush(hq,num)

cnt = 0
# 최소값 2개 꺼내고 더하기
# 더한 값 2개 다시 넣기
# M번 반복
while cnt < M:
    num1,num2 = heapq.heappop(hq),heapq.heappop(hq)
    sum_val = num1+num2
    heapq.heappush(hq,sum_val)
    heapq.heappush(hq,sum_val)
    cnt += 1

ans = 0
for val in hq:
    ans += val

print(ans)
