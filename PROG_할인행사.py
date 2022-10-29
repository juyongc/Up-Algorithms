def solution(want, number, discount):
    answer = 0
    
    item_dict = {}
    for i in range(len(want)):
        item_dict[want[i]] = number[i]
    
    s,e = 0,0
    total = 0
    # 투포인터 사용
    while s <= e:
        # 백트래킹 - max index 넘지 않도록
        if e >= len(discount):
            break
        item = discount[e]
        # item이 없는 품목이면 => 현재 인덱스까지 바로 오고 item_dict 복구
        if item not in item_dict:
            e += 1
            s = e
            total = 0
            for i in range(len(want)):
                item_dict[want[i]] = number[i]
            continue
        # 이미 다 샀으면 => s 한칸씩 올리면서 갱신
        while item_dict[item] <= 0:
                now = discount[s]
                item_dict[now] += 1
                s += 1
                total -= 1
        # e부분 갱신
        item_dict[item] -= 1
        e += 1
        total += 1
        # 다 샀으면 => 정답 +1
        if total == 10:
            answer += 1
    
    return answer