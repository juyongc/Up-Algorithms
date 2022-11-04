def solution(topping):
    answer = 0
    bro_topping_cnt = 0
    bro = {}
    # 모든 토핑 개수 카운팅
    for top in topping:
        if top in bro:
            bro[top] += 1
        else:
            bro[top] = 1
            bro_topping_cnt += 1
            
    su = set()
    # 철수가 한조각씩 더 가져감
    for top in topping:
        bro[top] -= 1
        if top not in su:       # 철수한테 없던 토핑이면 => 추가
            su.add(top)
        if bro[top] == 0:       # 동생한테 있던 마지막 토핑이면 => 동생 토핑 --
            bro_topping_cnt -= 1
        # 철수와 동생 토핑 수가 같으면 => answer ++
        if bro_topping_cnt == len(su):
            answer += 1
            
    return answer