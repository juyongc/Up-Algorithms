import sys


def dfs(a,b,c):
    global plate,dx,dy
    color = plate[a][b]
    now = 1
    stack = [(a,b)]         # 스택
    collect = [(a,b)]       # 왼쪽 정렬 위한 바둑 위치 모음
    while stack:
        x,y = stack.pop()
        if 0<=x+dx[c]<21 and 0<=y+dy[c]<21:     # 바둑판 내에서
            if plate[x+dx[c]][y+dy[c]] == color:    # 기존과 같은 색 바둑돌이라면
                stack.append(((x+dx[c]),(y+dy[c])))
                collect.append(((x+dx[c]),(y+dy[c])))
                now += 1
    if now == 5:                                    # 5개만 인정함
        collect.sort(key=lambda x: x[1])            # 왼쪽 정렬
        return color,collect[0][0],collect[0][1]
    else:
        return 0,a,b


inputs = sys.stdin.readline
plate = []              # 바둑판
# 조건 검색 쉽게 하기 위해 판을 20x20으로 만들기
plate.append([0]*21)
for _ in range(19):
    arr = [0] + list(map(int,inputs().split())) + [0]
    plate.append(arr)
plate.append([0] * 21)
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
flag = 0    # 정답 체크용
ans = 0     # 승부 결과

for i in range(21):
    for j in range(21):
        if plate[i][j]!= 0:
            for k in range(8):
                if plate[i+dx[k]][j+dy[k]] != plate[i][j] and plate[i+dx[7-k]][j+dy[7-k]] == plate[i][j]:
                    ans,px,py = dfs(i,j,7-k)    # 승부 결과 / 위치(x,y)
                    if ans != 0:
                        flag = 1
                        break
            if flag == 1:
                break
    if flag == 1:
        break

# 조건에 따른 출력
print(ans)
if ans != 0:
    print(px,py)
