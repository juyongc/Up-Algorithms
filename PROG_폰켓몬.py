def solution(nums):
    answer = 0
    tot = len(nums) // 2
    kinds = dict()
    
    # 모든 수 중복 확인
    for num in nums:
        if num in kinds:
            kinds[num] += 1
        else:
            kinds[num] = 1
    
    answer = len(kinds)
    
    # 최대값보다 크면 => answer = 최대값
    if answer > tot:
        answer = tot
    
    return answer