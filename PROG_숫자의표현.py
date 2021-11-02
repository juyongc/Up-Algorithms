from collections import deque
def solution(n):
    answer = 0
    q = deque()
    now = 0
    # 1~n까지 숫자 넣기
    for i in range(1,n+1):
        now += i
        q.append(i)
        # 현재값이 n보다 크면 => FIFO
        while now > n:
            val = q.popleft()
            now -= val
        if now == n:    # 현재값 == n => 카운팅 ++
            answer += 1
            
    return answer