import sys
inputs = sys.stdin.readline

K,N = map(int,input().split())
cables = [int(input()) for _ in range(K)]
cables.sort()
ans = 0

s,e = 1,cables[-1]

# 이분탐색
while s <= e:
    mid = (s+e) // 2
    num = 0
    for cable in cables:
        num += cable // mid

    if num >= N:
        ans = max(ans,mid)
        s = mid + 1
    else:
        e = mid - 1

print(ans)
