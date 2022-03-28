def solution(routes):
    answer = 0
    routes.sort(reverse=True)       # reverse로 정렬
    # 모든 라우터 값 비교
    while routes:
        s,e = routes.pop()          # 현재 가장 진입 빠른 차 꺼내기
        while routes:
            ns,ne = routes.pop()    # 다음으로 진입 빠른 차 꺼내기
            if ns <= e:         
                s = ns
            else:                       # 가장 진입 빠른 차 범위 밖이면 다시 추가
                routes.append([ns,ne])
                break
            if ne <= e:
                e = ne
        answer += 1
    return answer