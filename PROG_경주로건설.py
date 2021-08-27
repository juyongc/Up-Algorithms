def solution(board):
    road = board
    row = len(road)
    # 4방향 탐색
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 위치별 최소값 저장용
    compare = [[99999999999] * row for _ in range(row)]
    q = deque()
    # 초기값 세팅
    if road[0][1] == 0:
        q.append((0, 1, 2, 1))
        compare[0][1] = 1
    if road[1][0] == 0:
        q.append((1, 0, 0, 1))
        compare[1][0] = 1
    compare[0][0] = 0
    
    while q:
        x, y, pos, val = q.popleft()    # 현 위치,방향,값
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 내 + 빈 칸이면
            if 0 <= nx < row and 0 <= ny < row and road[nx][ny] == 0:
                if k == pos:
                    now = val + 1
                else:
                    now = val + 6
                # 위치에 저장된 값보다 작거나 같아야 함
                if compare[nx][ny] >= now:
                    compare[nx][ny] = now
                    q.append((nx, ny, k, now))

    answer = (compare[row - 1][row - 1]) * 100

    return answer