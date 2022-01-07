import sys
inputs = sys.stdin.readline


# 현재값, 인덱스 위치
def subseq(cur_sum,now):
    global ans

    if cur_sum == S:            # S면 ans ++
        ans += 1

    for i in range(now+1,N):    # 현재 인덱스 이후값만 방문
        if visit[i] == 1:
            continue
        else:
            cur_sum += nums[i]
            visit[i] = 1
            subseq(cur_sum,i)
            cur_sum -= nums[i]
            visit[i] = 0


N,S = map(int,inputs().split())
nums = list(map(int,inputs().split()))

visit = [0] * N
ans = 0

for k in range(N):
    visit[k] = 1
    subseq(nums[k],k)
    visit[k] = 0

print(ans)
