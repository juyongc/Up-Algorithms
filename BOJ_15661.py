import sys
from itertools import combinations
inputs = sys.stdin.readline

N = int(input())
ability = []
for _ in range(N):
    ability.append(list(map(int,inputs().split())))

mini = 9999999999
# 1 ~ N까지 팀조합 구해서 계산
for i in range(1,N):
    team1 = list(combinations([k for k in range(N)],i))
    # team: team1 중 하나
    # counter: team1에 속하지 않은 팀원
    for team in team1:
        counter = []
        score1 = 0      # team1 능력치                      
        for j in range(len(team)):
            for k in range(len(team)):
                score1 += ability[team[j]][team[k]]
        now = 0
        # counter 팀 구하기
        for x in range(N):
            if len(team) <= now:
                counter.append(x)
                continue
            if team[now] != x:
                counter.append(x)
            else:
                now += 1

        score2 = 0      # counter팀 능력치
        for j in range(len(counter)):
            for k in range(len(counter)):
                score2 += ability[counter[j]][counter[k]]
        mini = min(mini,abs(score2 - score1))   # 최소값 갱신

print(mini)