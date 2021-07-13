import sys

inputs = sys.stdin.readline
N,R,C = map(int,inputs().split())
tot = 0
x = 2**N

# x에서 x//2 값을 기준으로
# 좌/우 확인 -> 오른쪽이면 (x//2) * (x//2) 만큼 한 뒤에 해당 영역 진입
# 위/아래 확인 -> 아래면 x * (x//2) 한 뒤 해당 영역 진입
# 계산 후, x를 반으로 나눠서 더 작은 영역에서 반복
while x > 1:
    if C >= x//2:
        tot += (x//2) * (x//2)
        C -= x//2
    if R >= x//2:
        tot += (x//2) * x
        R -= x//2
    x = x//2

print(tot)