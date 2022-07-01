import sys
inputs = sys.stdin.readline

N = int(input())
developer = list(map(int,inputs().split()))

s,e = 0,N-1
ans = 0
# 두 개발자 중에서 능력치가 작은 개발자 변경
while s < e:
    cnt = e - s - 1
    now = min(developer[s],developer[e]) * cnt
    ans = max(ans, now)

    if developer[s] <= developer[e]:
        s += 1
    else:
        e -= 1

print(ans)
