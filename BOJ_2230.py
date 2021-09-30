import sys
inputs = sys.stdin.readline

N,M = map(int,input().split())
nums = [int(inputs().rstrip()) for _ in range(N)]
nums.sort()
s,e = 0,0
mini = 999999999999999999

# 투포인터 활용
while s < N-1:
    ns = nums[s]
    ne = nums[e]
    if ne - ns >= M:                # 일정 수 이상이면
        mini = min(mini,ne - ns)    # 최소값 확인
        if mini == M:
            break
        s += 1                      # 시작점 + 1
    else:                           # 아니면 => 끝점 + 1
        e += 1
    if e == N:
        break

print(mini)
