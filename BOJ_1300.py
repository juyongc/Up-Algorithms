N = int(input())
K = int(input())
s,e = 1,K
# 이분탐색
while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in range(1,N+1):
        if i > mid: # i가 더 크면 => 이후는 0임
            break
        # min값 더하기
        cnt += min(mid // i,N)
    # s,e 갱신
    if cnt >= K:
        e = mid - 1
        ans = mid
    else:
        s = mid+1

print(ans)
