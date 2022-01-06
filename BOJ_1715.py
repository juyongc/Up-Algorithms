import sys
import heapq
inputs = sys.stdin.readline

N = int(input())
card_nums = []
for _ in range(N):
    heapq.heappush(card_nums,int(inputs().strip()))

ans = 0

# 카드 묶음 수가 1보다 크면
# 가장 작은 값 2개를 꺼내서 더한 뒤, 다시 heapq에 추가
while len(card_nums) > 1:
    pick1 = heapq.heappop(card_nums)
    pick2 = heapq.heappop(card_nums)
    combo = pick1 + pick2
    ans += combo
    heapq.heappush(card_nums, combo)

print(ans)
