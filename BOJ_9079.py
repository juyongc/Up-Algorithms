import sys
inputs = sys.stdin.readline

# 모든 가능한 경우의 수 구하기
def checkPosition(num,cnt):
    global answer,visit

    if num > 7:
        final = changeCoins(visit)
        s = final[0]
        for i in range(9):
            if final[i] != s:
                return
        answer = min(answer,cnt)
        return

    checkPosition(num+1, cnt)
    visit[num] = 1
    checkPosition(num+1,cnt+1)
    visit[num] = 0

# 방문체크된 코인만 바꾸기
def changeCoins(visit):
    global coins,over
    check = coins[:]
    for i in range(8):
        if visit[i] == 1:
            now = over[i]
            for j in range(3):
                if check[now[j]] == "H":
                    check[now[j]] = "T"
                else:
                    check[now[j]] = "H"
    return check


N = int(input())
for _ in range(N):
    coins = []
    for _ in range(3):
        cur_coin = list(inputs().split())
        coins += cur_coin

    answer = 999999999999999
    visit = [0]*8
    # 한번에 변경되는 코인들
    over = {
        0: [0, 1, 2],
        1: [3, 4, 5],
        2: [6, 7, 8],
        3: [0, 3, 6],
        4: [1, 4, 7],
        5: [2, 5, 8],
        6: [0, 4, 8],
        7: [2, 4, 6]
    }
    checkPosition(0, 0)
    if answer == 999999999999999:
        answer = -1
    print(answer)

