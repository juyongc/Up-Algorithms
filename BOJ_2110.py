import sys
inputs = sys.stdin.readline

N,C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

s = 1
e = arr[-1] - arr[0]

# 이분탐색
while s <= e:
    mid = (s+e) // 2

    cnt = 1
    now = 0
    # 마지막 집까지 가면서 최대 거리보다 크면 갱신
    for i in range(1,N):
        distance = arr[i] - arr[now]
        if distance >= mid:
            cnt += 1
            now = i

    if cnt >= C:        # 카운팅 수가 많음
        s = mid + 1     # => 시작값 늘림
        ans = mid
    else:               # 카운팅 수 적음
        e = mid - 1     # => 끝값 줄임

print(ans)