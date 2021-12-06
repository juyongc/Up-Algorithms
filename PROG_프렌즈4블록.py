from collections import deque
def solution(m, n, B):
    answer = 0
    check = 0
    
    board = []
    # 문자열 잘라서 문자로 만들기
    for b in B:
        board.append(list(b))
    
    dx = [1,1,0]
    dy = [0,1,1]
    # 새로운 빈칸이 없을 때까지 반복
    while check == 0:
        
        q = deque()
        # 4칸 같은 부분 있는지 체크
        for i in range(m-1):
            for j in range(n-1):
                flag = 0
                now = board[i][j]
                if now == 0:    # 이미 빈칸이면 pass
                    continue
                    
                for k in range(3):  # 우,하,대각 같은지 확인
                    x,y = i+dx[k],j+dy[k]
                    if now == board[x][y]:
                        flag += 1
                    else:
                        break
                if flag == 3:       # 같으면 q에 추가
                    q.append((i,j))
                    for k in range(3):
                        x,y = i+dx[k],j+dy[k]
                        q.append((x,y))
        # 새로운 빈칸 없으니 나가기
        if not q:
            check = 1
            break
            
        while q:    # 같은 부분 빈칸 만들기
            a,b = q.popleft()
            board[a][b] = 0
        
        # 열마다 빈칸 있는지 확인
        for i in range(n):
            new_line = deque()
            cnt = 0
            for j in range(m):
                if board[j][i] != 0:
                    new_line.append(board[j][i])
                else:
                    cnt += 1
            
            if cnt == 0:    # 빈칸 없으면 pass
                continue
            
            for j in range(m):
                if cnt > 0:     # 빈칸 있으면 => 빈칸 먼저
                    board[j][i] = 0
                    cnt -= 1
                else:           # 빈칸 없으면 => 그대로 내려오기
                    now = new_line.popleft()
                    board[j][i] = now

    # 빈칸 카운팅
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer