import sys
from collections import defaultdict
inputs = sys.stdin.readline


N,K = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
pre_fix = [0]*N
pre_fix[0] = nums[0]

check = defaultdict(int)
for i in range(N):
    # 첫번째 값과 그 외 누적합 구하기
    if i == 0:
        pre_fix[i] = nums[i]
    else:
        pre_fix[i] = pre_fix[i-1] + nums[i]
    if pre_fix[i] == K:     # 현재 누적합 == K
        cnt += 1
    # 현재 값 - K 가 있으면 => 그만큼 ++
    cnt += check[pre_fix[i]-K]
    check[pre_fix[i]] += 1

print(cnt)
