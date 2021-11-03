import sys
inputs = sys.stdin.readline

N = int(input())
sol = list(map(int,inputs().split()))

sol.sort()

s,e = 0,N-1
mini = 999999999999999999
a1,a2 = 0,0
# 두 포인터
# 끝과 끝에서 시작해서 
# 결과가 0보다 작으면 => s++
# 0보다 크면 => e --
while s < e:
    now = sol[s]+sol[e]
    if abs(now) < mini:
        mini = abs(now)
        a1,a2 = sol[s],sol[e]
    if now < 0:
        s += 1
    else:
        e -= 1

print('{0} {1}'.format(a1,a2))