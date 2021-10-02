import sys
inputs = sys.stdin.readline

N,S = map(int,inputs().split())
nums = list(map(int,inputs().split()))

ans = 0     # 정답
s,e = 0,0
tot = nums[0]           # 부분합
mini = 999999999999999  # 최소 길이
# 투포인터 사용
while e < N:
    if tot < S:
        e += 1
        if e >= N:
            break
        tot += nums[e]
    else:
        mini = min(mini,e-s+1)
        tot -= nums[s]
        s += 1
        
if mini != 999999999999999:
    ans = mini

print(ans)