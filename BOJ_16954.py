import sys
from collections import deque

# BFS 탐색
def bfs():
    # 초기 큐 설정
    q = deque()
    q.append([7,0])

    cnt = 1         # 벽 움직임까지 남은 탐색
    next_cnt = 0    # 다음 벽 움직임까지 남은 탐색
    # 큐에 값이 남아있다면
    while q:
        x,y = q.popleft()
        cnt -= 1    # 다음 벽 움직임까지 -1
        if blocks[0][0] >= 7:   # 가장 앞 벽이 7이상이면 => 탐색 가능
            return 1
        # 9방향 탐색
        for k in range(9):
            cx = x+dx[k]
            cy = y+dy[k]
            check = 1   # 큐에 삽입 가능한지 체크용
            if 0<=cx<8 and 0<=cy<8:
                for block in blocks:
                    if block[0] > 7:    # 벽이 7 이상이면 다음벽부터는 탐색 필요 X
                        break
                    # 현재 위치 또는 현재 위치의 윗 행에 벽이 있다면
                    if block == [cx,cy] or block == [cx-1,cy]:
                        check = 0   # 체크값 => 0
                        break

                if check == 1:          # 체크값이 1이면,
                    q.append([cx,cy])   # 큐에 append
                    next_cnt += 1       # 다음 cnt 값 + 1
        # cnt == 0 => 벽 움직임
        if cnt == 0:
            cnt = next_cnt  # 다음 벽 움직임까지 카운트 = next_cnt
            next_cnt = 0    # next_cnt 초기화
            # 벽이 움직였으니까, 벽의 row값 +1 해주기
            for block in blocks:
                # 현재 벽이 7보다 크면, 다음벽해줄 필요 없음
                if block[0] > 7:
                    break
                block[0] += 1
    return 0


inputs = sys.stdin.readline

plates = [list(inputs().rstrip()) for _ in range(8)]

blocks = []
# 벽 찾기
for i in range(8):
    for j in range(8):
        if plates[i][j] == '#':
            blocks.append([i,j])
# 9방향 탐색
dx = [0,0,0,1,1,1,-1,-1,-1]
dy = [0,1,-1,0,1,-1,0,1,-1]

if len(blocks) > 0:     # 벽이 있다면
    ans = bfs()
else:                   # 벽이 없다면
    ans = 1

print(ans)