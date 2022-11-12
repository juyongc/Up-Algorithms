import sys
inputs = sys.stdin.readline

N,K,D = map(int,inputs().split())
box = [list(map(int,inputs().split())) for _ in range(K)]

s,e = 1,N
# lower bound 이분탐색
# 모든 상자를 이분탐색의 mid 값을 기준으로 해당 값까지 얼마만큼 저장할 수 있는지 비교
while s < e:
    mid = (s+e)//2
    cnt = 0
    for bs,be,bm in box:
        if bs > mid:
            continue

        end_point = min(be,mid)
        start_point = bs

        cnt += ((end_point - start_point) // bm + 1)
        if cnt >= D:
            break

    if cnt >= D:
        e = mid
    else:
        s = mid + 1

answer = s
print(answer)
