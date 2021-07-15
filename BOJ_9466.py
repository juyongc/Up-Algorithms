import sys
sys.setrecursionlimit(10**6)

def find(x):
    global team
    check[x] = 1
    cycle.append(x)
    y = parent[x]

    if check[y] == 0:   # 아직 팀이 없다면
        find(y)
    else:               # 팀이 있다면
        if y in cycle:  # 사이클 여부확인
            start = cycle.index(y)  # 사이클 최초 시작점 찾기
            team += cycle[start:]   # 팀에 현재 팀 인원 넣기
        return

inputs = sys.stdin.readline

T = int(inputs())
for _ in range(T):
    N = int(inputs())
    parent = [0] + list(map(int,inputs().split()))
    check = [0]*(N+1)   # 팀 여부 체크된 리스트
    team = []           # 전체 팀 멤버 수 체크용
    for i in range(1,N+1):
        if check[i] == 0:
            cycle = []
            find(i)

    print(N - len(team))