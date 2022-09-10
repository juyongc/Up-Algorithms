from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    
    num = 2*(len(queue1) + len(queue2))
    total = sum(queue1) + sum(queue2)
    
    cnt = 0
    while q1_sum != q2_sum:
        if cnt >= num:
            break
        if q1_sum > q2_sum:
            now = q1.popleft()
            q2.append(now)
            q1_sum -= now
            q2_sum += now
        elif q1_sum < q2_sum:
            now = q2.popleft()
            q1.append(now)
            q2_sum -= now
            q1_sum += now
        cnt += 1
    
    if cnt >= num:
        answer = -1
    else:
        answer = cnt
    
    return answer