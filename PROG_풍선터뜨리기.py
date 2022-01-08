def solution(a):
    answer = 0
    
    answer += 2     # 양 끝
    
    right_min = [a[-1]]*len(a)
    # 오른쪽 min값 찾기
    for i in range(len(a)-2,-1,-1):
        if right_min[i+1] > a[i]:
            right_min[i] = a[i]
        else:
            right_min[i] = right_min[i+1]
    left_min = a[0]
    
    # smaller/기준/smaller <= 불가능
    # 왼쪽,오른쪽 min값 확인 => 양쪽다 작으면 불가
    # 아니면 answer ++
    for i in range(1,len(a)-1):
        small_num = 0
        if a[i] < left_min:
            left_min = a[i]
        else:
            small_num += 1
        
        if a[i] > right_min[i]:
            small_num += 1
        
        if small_num < 2:
            answer += 1
        
    return answer