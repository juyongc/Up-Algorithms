import sys
inputs = sys.stdin.readline

N = int(input())
arr = list(map(int,inputs().split()))
arr.sort()

now = 1
# 이전 모든 값의 합+1 < 현재값
# 더 이상 만들 수 없음
for a in arr:
    if now < a:
        break
    now += a

print(now)