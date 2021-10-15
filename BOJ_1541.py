import sys
inputs = sys.stdin.readline

eqn = input().split('-')
ans = 0
for i in range(len(eqn)):
    vals = eqn[i].split('+')
    now = 0
    for val in vals:        # 모든 내부 값 더하기
        now += int(val)
    # 첫번째 값을 제외하고는 '-' 안 괄호로 생각하기
    if i == 0:
        ans += now
    else:
        ans -= now

print(ans)