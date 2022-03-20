def solution(money):
    answer = 0
    first_v = [[0,0] for _ in range(len(money)-1)]
    last_v = [[0,0] for _ in range(len(money)-1)]
    first_v[0][0] = money[0]
    first_v[1][0] = money[1]
    first_v[1][1] = first_v[0][0]
    # 첫 집 방문
    for i in range(2,len(money)-1):
        first_v[i][0] = max(first_v[i-1][1],first_v[i-2][1]) + money[i]
        first_v[i][1] = first_v[i-1][0]
        
    last_v[0][0] = money[1]
    last_v[1][0] = money[2]
    last_v[1][1] = last_v[0][0]
    # 첫 집 방문X
    for i in range(2,len(money)-1):
        last_v[i][0] = max(last_v[i-1][1],last_v[i-2][1]) + money[i+1]
        last_v[i][1] = last_v[i-1][0]
    answer = max(first_v[-1][0],first_v[-1][1],last_v[-1][0],last_v[-1][1])
    return answer