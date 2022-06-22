import sys
inputs = sys.stdin.readline

N,C = map(int,input().split())
house = [int(inputs()) for _ in range(N)]
house.sort()

# 최대 개수 가능한 시작,끝점
s = 1
e = house[-1] - house[0]

maxi = 0
while s <= e:
    mid = (s+e) // 2    # 현재 추정한 최대 개수
    cnt = 1             # 공유기 설치 카운팅
    now = 0             # 공유기 설치 시작점
    # C개 설치가능한지 확인
    for i in range(1,N):
        if house[i] - house[now] >= mid:
            cnt += 1
            now = i
        if cnt >= C:
            break
    # 상황별 최대 개수 설정 변경
    if cnt >= C:
        maxi = max(maxi,mid)
        s = mid + 1
    else:
        e = mid - 1

print(maxi)
