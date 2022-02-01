def solution(gems):
    answer = [1,len(gems)]
    gem_kinds = {}
    gem_cnt = 0
    # 보석 개수 구하기 및 초기화
    for gem in gems:
        if gem not in gem_kinds:
            gem_kinds[gem] = 0
            gem_cnt += 1
    
    s,e = 0,0
    cnt = 0
    # 투포인터 이용하기
    while e < len(gems):
        
        now = gems[e]
        if gem_kinds[now] == 0:
            gem_kinds[now] = 1
            cnt += 1
        elif gem_kinds[now] > 0:
            gem_kinds[now] += 1
        # 총 보석개수만큼 모였으면 => s ++
        while cnt >= gem_cnt:
            cur_area = e - s
            bef_area  = answer[1] - answer[0]
            if cur_area < bef_area:
                answer = [s+1,e+1]
            elif cur_area == bef_area:
                if s+1 < answer[0]:
                    answer = [s+1,e+1]
            if s < e:
                cur = gems[s]
                gem_kinds[cur] -= 1
                if gem_kinds[cur] == 0:
                    cnt -= 1
                s += 1
            else:
                break
        e += 1  # e ++
        
    return answer