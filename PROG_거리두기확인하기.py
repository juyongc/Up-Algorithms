def solution(places):
    answer = [1]*5
    
    for num in range(5):    # 대기실 개수 = 5개
        answer[num] = bfs(places[num])
    
    return answer
    
    
def bfs(arr):
    apply = []
    
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                # 현재 x,y, 탐색 횟수, 원 x,y
                apply.append((i,j,0,i,j))
    # 4방향 탐색           
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while apply:
        # 현재 x,y, 탐색 횟수, 원 x,y
        x,y,pos,px,py = apply.pop()     

        for k in range(4):
            a = x +dx[k]
            b = y +dy[k]
            if 0<=a<5 and 0<=b<5:
                if arr[a][b] == 'P':    # 근처 사람이면 => 0 반환
                    if px != a or py != b:
                        return 0
                elif arr[a][b] == 'X':  # 파티션이면 해당 방향 탐색 중단
                    continue
                else:
                    if pos == 0:        # 첫 탐색이면 다음 탐색 위해 append
                        apply.append((a,b,pos+1,x,y))
                        
    return 1