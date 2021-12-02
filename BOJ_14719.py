import sys
inputs = sys.stdin.readline

H,W = map(int,inputs().split())
height = list(map(int,inputs().split()))

max_h = 0   # 가장 높은 블럭 높이
idx = 0     # 가장 높은 블럭 위치
wall = 0    # 총 블럭 개수
# 가장 높은 블럭 위치 찾기
for i in range(W):
    wall += height[i]
    if height[i] > max_h:
        max_h = height[i]
        idx = i

max_l,max_r = 0,0   # 가장 높은 블럭 기준 왼/오 높은 블럭 개수
tot = 0             # 모든 물의 양
# 왼쪽 ~ 가장 높은 벽까지 모든 물의 양
for i in range(idx):
    if height[i] > max_l:
        max_l = height[i]
    tot += max_l
# 가장 높은 벽 ~ 오른쪽까지 모든 물의 양
for i in range(W-1,idx-1,-1):
    if height[i] > max_r:
        max_r = height[i]
    tot += max_r

ans = tot - wall    # 전체 물의 양 - 전체 블럭 개수
print(ans)