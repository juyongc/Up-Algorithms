from collections import deque

def solution(game_board, table):
    answer = 0
    
    blocks = {}
    visit = [[0]*len(table[0]) for _ in range(len(table))]
    
    # 테이블에서 블록 형태 구하기
    def bfs(a,b):
        q = deque()
        q.append((a,b))

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        min_x = a
        min_y = b
        find_block = [[a,b]]
        while q:
            x,y = q.popleft()
            for k in range(4):
                xx,yy = x + dx[k], y + dy[k]
                if 0<=xx<len(table) and 0<=yy<len(table[0]) and visit[xx][yy] == 0 and table[xx][yy] == 1:
                    visit[xx][yy] = 1
                    min_x = min(xx,min_x)
                    min_y = min(yy,min_y)
                    q.append((xx,yy))
                    find_block.append([xx,yy])
                    
        for k in range(len(find_block)):
            find_block[k][0] -= min_x
            find_block[k][1] -= min_y
            
        find_block.sort()
        
        return len(find_block),find_block 
    
    # 테이블의 모든 블록 위치 구하고 bfs
    for i in range(len(table)):
        for j in range(len(table[0])):
            if visit[i][j] == 0 and table[i][j] == 1:
                visit[i][j] = 1
                cnt,block_pos = bfs(i,j)
                
                if cnt in blocks:
                    blocks[cnt].append(block_pos)
                else:
                    blocks[cnt] = [block_pos]
    
    game_visit = [[0]*len(game_board[0]) for _ in range(len(game_board))]

    # 테이블에서 블록 형태 구하기
    def game_bfs(a,b):
        q = deque()
        q.append((a,b))

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        min_x = a
        min_y = b
        find_block = [[a,b]]
        while q:
            x,y = q.popleft()
            for k in range(4):
                xx,yy = x + dx[k], y + dy[k]
                if 0<=xx<len(game_board) and 0<=yy<len(game_board[0]) and game_visit[xx][yy] == 0 and game_board[xx][yy] == 0:
                    game_visit[xx][yy] = 1
                    min_x = min(xx,min_x)
                    min_y = min(yy,min_y)
                    q.append((xx,yy))
                    find_block.append([xx,yy])
        max_x,max_y = 0,0
        for k in range(len(find_block)):
            find_block[k][0] -= min_x
            find_block[k][1] -= min_y
            
            max_x = max(max_x,find_block[k][0])
            max_y = max(max_y,find_block[k][1])
            
        find_block.sort()
        
        return len(find_block),find_block,max_x,max_y 
    
    # 게임보드 퍼즐 조각 가능 위치 0,90,180,270 회전 후 비교
    def rotate(puzzle,arr,mmx,mmy):
        
        rot = 0
        while rot < 4:
            mat = []
            flag = 0
            if rot == 0:
                for puz in puzzle:
                    puz_x = puz[0]
                    puz_y = puz[1]
                    mat.append([puz_x,puz_y])
            elif rot == 1:
                for puz in puzzle:
                    puz_x = puz[1]
                    puz_y = mmx - puz[0]
                    mat.append([puz_x,puz_y])
            elif rot == 2:
                for puz in puzzle:
                    puz_x = mmx - puz[0]
                    puz_y = mmy - puz[1]
                    mat.append([puz_x,puz_y])
            else:
                for puz in puzzle:
                    puz_x = mmy - puz[1]
                    puz_y = puz[0]
                    mat.append([puz_x,puz_y])
            mat.sort()
            for i in range(len(puzzle)):
                if mat[i] != arr[i]:
                    flag = 1
                    break
            if flag == 0:
                return True
            
            rot += 1
            
        return False

    # 게임 보드의 블록 조각 위치 구하고 bfs
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and game_visit[i][j] == 0:
                game_visit[i][j] = 1
                cnt,block_pos,mx,my = game_bfs(i,j)
                
                if cnt in blocks:
                    if blocks[cnt] == []:
                        continue
                    for z in range(len(blocks[cnt])):
                        bol = rotate(block_pos,blocks[cnt][z],mx,my)
                        if bol:
                            answer += cnt
                            blocks[cnt].pop(z)
                            break

    return answer