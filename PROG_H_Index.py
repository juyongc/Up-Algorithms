def solution(citations):
    answer = 0
    
    check = [0]*1001    # 0~1000까지 h편 이상 인용논문 카운팅 리스트
    # 해당 횟수 인용논문 카운팅
    for citation in citations:
        if 0<= citation < 1000:
            check[citation] += 1
        else:
            check[1000] += 1
    # 이전값 += 다음값
    for i in range(1000,0,-1):
        check[i-1] += check[i]
    # 1000부터 h번 이상 인용된 논문이 h편 이상인 h 찾기
    for i in range(1000,-1,-1):
        now = i
        upper = check[i]
        if upper >= now:
            answer = now
            break

    return answer