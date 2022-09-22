import sys
inputs = sys.stdin.readline

N,M,L = map(int,inputs().split())
store = [0] + list(map(int,inputs().split())) + [L]
store.sort()

end_area = 9999999
# 현재 휴게소의 최대 거리의 최소값 구하기
for i in range(1,len(store)):
    end_area = max(end_area, store[i] - store[i-1])

max_min = end_area
s,e = 1,end_area
# 매개 변수 탐색
while s <= e:
    mid = (s+e) // 2
    tot = 0
    flag = 1
    for i in range(1, len(store)):
        # store[i] ~ store[i-1] 거리 설치 가능한 구역 개수 구하기
        # 양 끝이 설치되어 있으니 - 1
        share = (store[i] - store[i-1] - 1) // mid
        tot += share
        if tot > M:
            flag = 0
            break

    if flag:
        max_min = mid
        e = mid - 1
    else:
        s = mid + 1

print(max_min)