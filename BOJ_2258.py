import sys
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
meat = [list(map(int,inputs().split())) for _ in range(N)]
meat.sort(key=lambda x:(x[1],-x[0]))    # 가격 오름차순, 무게 내림차순

cost = 9999999999999999
amount, same_price = 0, 0

# 덩어리 양 계속 갱신
# 가격 미만만 공짜 => 같은 가격이면 돈 내야함
# same_price로 같은 같은 가격 계산해놓기
for i in range(N):
    ma, mc = meat[i]
    amount += ma
    if i > 0 and meat[i-1][1] == mc:
        same_price += meat[i][1]
    else:
        same_price = 0
    if amount >= M:
        cost = min(cost, mc + same_price)
if cost == 9999999999999999:
    cost = -1

print(cost)
