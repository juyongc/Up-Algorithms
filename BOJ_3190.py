import sys
inputs = sys.stdin.readline

N = int(inputs().rstrip())
boards = [[0] * N for _ in range(N)]
# 사과 위치
K = int(inputs().rstrip())
for _ in range(K):
    aa, ab = map(int, inputs().split())
    boards[aa - 1][ab - 1] = 2
# 위치 변화 예정
L = int(inputs().rstrip())
change = []
for _ in range(L):
    ca, cb = inputs().split()
    change.append((int(ca), cb))
# 뱀 위치
bam = [(0, 0)]
visit = [[0] * N for _ in range(N)]
visit[0][0] = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
cnt = 0     # 움직인 시간
now = 2     # 현재 이동 경로
while True:
    x, y = bam[-1]
    nx, ny = x + dx[now], y + dy[now]
    cnt += 1
    # 조건에 맞으면 => 이동
    if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        if boards[nx][ny] == 2:     # 사과면 => 몸 길이 늘리기
            boards[nx][ny] = 0
            bam.append((nx, ny))
        else:                       # 사과 아니면 => 앞으로 가고 / 꼬리 자르기
            a, b = bam.pop(0)
            visit[a][b] = 0
            bam.append((nx, ny))
    else:           # 조건 안맞으면 => break
        break
    if change:      # 움직일 시간되면 => 움직이기
        if change[0][0] == cnt:
            if change[0][1] == 'D':
                now += 1
            else:
                now -= 1
            change.pop(0)
            now = now % 4

print(cnt)