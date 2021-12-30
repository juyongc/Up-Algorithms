def solution(stones, k):
    answer = 0
    s,e = 1,max(stones)
    
    # 이분 탐색
    while s <= e:
        mid = (s+e) // 2
        cnt = 0
        flag = 0
        # 징검다리 값과 mid값 비교
        for i in range(len(stones)):
            if mid >= stones[i]:    # mid가 크거나 같으면 => cnt += 1
                cnt += 1
            else:                   # mid가 작으면 => cnt = 0
                cnt = 0     
                if len(stones)-i <= k:  # 남은 값이 의미없으면 => break
                    break
            if cnt >= k:            # 못 건너면 => answer 갱신
                answer = mid
                flag = 1
                break
        # 상황에 따라 s,e 갱신
        if flag == 0:
            s = mid + 1
        else:
            e = mid - 1
            
    return answer