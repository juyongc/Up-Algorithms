def solution(n, t, m, ttab):
    answer = ''
    ntab = []       # 시간(int)값 넣을 리스트
    # 시간 숫자로 변경 => minute으로 맞추기
    # 시*60 + 분
    for val in ttab:
        ah, am = map(int, val.split(':'))
        ntab.append(ah * 60 + am)
    ntab.sort()     # 시간 오름차순 정렬
    s = 9 * 60      # 첫번째 버스값
    con = 0         # 콘 시간 정의
    ride = 0  # 현재까지 버스 이용 인원
    for i in range(n):
        onbus = 0   # 현재 버스 안 사람 수
        flag = 0    # 뒷 사람 유무 체크 플래그
        if i != 0:  # 버스 운행 간격 생각
            s += t
        # 정원만큼 탔는지 확인
        while onbus < m:
            if ride >= len(ntab):   # 모든 인원이 다 탔으면
                con = s             # 콘 탈 차례
                flag = 1 
                break
            if ntab[ride] <= s:     # 고객이 탑승 시간이내면
                onbus += 1          # 탑승 -> 현정원 +!, 전체정원 +1
                ride += 1
            else:  # 자리는 남았는데 그 시간 사람 없으면
                con = s     # 콘 차례 
                flag = 1
                break
        # flag가 0이면 -> 가장 뒷 승객보다 1분 빨리 타기
        if flag == 0:
            con = ntab[ride - 1] - 1
    # 시간을 시/분으로 맞추기
    hh = con // 60
    mm = con - hh * 60
    # 출력 형태에 따른 출력
    if hh < 10:
        answer += "0" + str(hh)
    else:
        answer += str(hh)
    answer += ":"
    if mm < 10:
        answer += "0" + str(mm)
    else:
        answer += str(mm)
    return answer