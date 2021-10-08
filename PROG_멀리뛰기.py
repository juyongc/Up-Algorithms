def solution(n):
    answer = 0
    
    nums = [0]*(n+1)
    
    nums[1] = 1
    # dp
    # 한칸전, 두칸전 값 더하기
    if n > 1:
        nums[2] = 1
    
        for i in range(2,n+1):
            nums[i] += nums[i-1]
            nums[i] += nums[i-2]
            
    answer = nums[n]
    return (answer % 1234567)