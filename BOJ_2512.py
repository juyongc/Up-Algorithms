import sys
inputs = sys.stdin.readline

N = int(inputs().rstrip())
costs = list(map(int,inputs().split()))
money = int(inputs().rstrip())
tot = sum(costs)
costs.sort()
if tot <= money:
    print(costs[-1])
else:
    s,e = 0,money
    answer = 0
    # 이분탐색
    while s <= e:
        mid = (s+e) // 2
        bud = 0
        for cost in costs:
            if cost >= mid:
                bud += mid
            else:
                bud += cost

        if bud > money:
            e = mid - 1
        else:
            ans = mid
            s = mid + 1
    print(ans)
