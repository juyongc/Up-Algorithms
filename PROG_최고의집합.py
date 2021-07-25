def solution(n, s):
    answer = []
    if 1*n > s:     # s가 1*n보다 작으면 불가능
        answer.append(-1)
    else:
        # n만큼 반복
        while n > 0:
            if s % n == 0:      # 나머지가 0이면
                now = s // n
            else:               # 나머지가 0이 아니면
                now = s//n + 1
            s -= now
            n -= 1
            answer.append(now)
    answer.sort()               # 오름차순 정리
    return answer