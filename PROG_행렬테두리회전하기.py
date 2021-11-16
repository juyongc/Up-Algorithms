from collections import deque
def solution(rows, columns, queries):
    answer = []
    arr = [[(j*columns+i) for i in range(1,columns+1)] for j in range(rows)]
    # 모든 쿼리 반복
    for query in queries:
        mini = 999999999        # 최소값
        x1,y1,x2,y2 = query     # 쿼리 - 리스트 조건에 맞게 -1
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        q = deque()
        # 테두리 숫자 큐에 삽입
        for i in range(y1,y2):
            q.append(arr[x1][i])
        for i in range(x1,x2):
            q.append(arr[i][y2])
        for i in range(y2,y1,-1):
            q.append(arr[x2][i])
        for i in range(x2,x1,-1):
            q.append(arr[i][y1])
        
        q.rotate(1)     # 시계 방향 회전
        # 테두리 숫자 갱신 & 최소값 탐색
        for i in range(y1,y2):
            arr[x1][i] = q.popleft()
            mini = min(mini,arr[x1][i])
        for i in range(x1,x2):
            arr[i][y2] = q.popleft()
            mini = min(mini,arr[i][y2])
        for i in range(y2,y1,-1):
            arr[x2][i] = q.popleft()
            mini = min(mini,arr[x2][i])
        for i in range(x2,x1,-1):
            arr[i][y1] = q.popleft()
            mini = min(mini,arr[i][y1])
            
        answer.append(mini)     # 최소값 정답에 삽입
        
    return answer