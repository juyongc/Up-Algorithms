def solution(n, times):
    answer = 0
    # 심사원이 한명이면 => 바로 답 찾기
    if len(times) == 1:
        answer = times[0] * n
    else:   # 여려명이면 => 이진탐색
        times.sort()
        mini = 0
        maxi = times[-1] * n
        while True:
            now = (mini + maxi) // 2    # 중간값
            need = 0                    # 총 검사 가능 인원 카운팅
            for time in times:
                need += now // time # 현재 총 검사 가능인원
            # 원하는 값보다 크거나 같으면 => 중간값-1 체크
            # '크거나' 포함 이유: 이후값이 나눠떨어져서 포함될 경우가 있음 
            if need >= n:           
                check = 0
                for time in times:
                    check += (now - 1) // time
                if check < n:       # (now-1) 체크값이 원하는 값보다 작으면 => 답임
                    answer = now
                    return answer
                else:               # 재탐색
                    maxi = now
            else:
                mini = now + 1

    return answer