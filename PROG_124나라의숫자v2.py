def solution(n):
    answer = ''
    # 3진법과 유사(0,1,2 => 4,1,2)
    # 3으로 나눠떨어지면 => 4 넣고, -1하기
    while n > 0:
        n,rem = divmod(n,3)
        if rem == 0:
            answer += "4"
            n -= 1
        else:
            answer += str(rem)
    
    answer = answer[::-1]
    
    return answer