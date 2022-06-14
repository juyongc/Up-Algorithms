import sys
inputs = sys.stdin.readline

N = int(input())
plan = [tuple(map(int,inputs().split())) for _ in range(N)]
plan.sort(key=lambda x: -x[1])      # 일 끝나는 시간 역으로 정렬

now = plan[0][1]
for work,fin in plan:
    delay = fin - now       # 최소 시작 시간과 일 끝내야하는 시간 비교해서 딜레이된 시간 확인
    if delay < 0:           # 0보다 작으면 여유 있는 거니까 리셋
        delay = 0
    now = fin - work - delay    # 현재시간 = 끝내야 하는 시간 - 필요한 시간 - 딜레이 시간
    if now < 0:
        break

if now < 0:
    now = -1
print(now)
