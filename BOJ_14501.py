import sys


def money(N,day,tot):
    global maxi
    # 내일로 넘기기
    if day >= N:
        if maxi < tot:
            maxi = tot
        return

    money(N, day + 1, tot)
    # 일하면 걸리는 시간 계산하고 넘기기
    if day + days[day][0] > N:
        if maxi < tot:
            maxi = tot
        return

    money(N,day+days[day][0], tot+days[day][1])


inputs = sys.stdin.readline

N = int(inputs())
days = [list(map(int,inputs().split())) for _ in range(N)]

maxi = 0

money(N,0,0)

print(maxi)