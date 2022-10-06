import sys
inputs = sys.stdin.readline


def move(x,y):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    stack = [(x,y)]      # 현재 위치
    route = [(x,y)]      # 이동동선 저장용
    flag = 0            # 탈출 확인용
    check = set()       # 현재 이동이 무한루프인지 확인용
    check.add((x,y))
    
    # 현재 위치에서 다음 위치 찾기
    while stack:
        a,b = stack.pop()
        word = maze[a][b]
        xx,yy = a + direction[word][0], b + direction[word][1]
        
        if 0<=xx<N and 0<=yy<M:
            if visit[xx][yy] == -1:         # 탈출 불가
                break
            elif visit[xx][yy] == 0:        # 탈출 여부 확인중
                if (xx,yy) in check:        # 무한루프 => 탈출 불가
                    break
                else:                       # 확인중
                    stack.append((xx,yy))
                    route.append((xx,yy))
                    check.add((xx,yy))
            else:                           # 탈출 가능
                flag = 1
                break
        else:
            flag = 1
            break
    
    if flag:    # 탈출 가능 => visit = 1
        for x,y in route:
            visit[x][y] = 1
    else:       # 탈출 불가 => visit = -1
        for x,y in route:
            visit[x][y] = -1


N,M = map(int,inputs().split())

maze = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

direction = {
    "U": (-1,0), "R": (0,1),
    "D": (1,0), "L": (0,-1)
}

# 미방문지면 탈출 가능여부 확인
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            move(i,j)

ans = 0
# 정답 개수 카운팅
for i in range(N):
    for j in range(M):
        if visit[i][j] == 1:
            ans += 1

print(ans)
