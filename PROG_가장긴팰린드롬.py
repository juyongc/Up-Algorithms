def solution(s):
    answer = 1

    N = len(s)  # 문자열에서 문자 개수
    # 모든 문자 확인
    for i in range(N):
        j = 1
        mid_o = 1
        # 팰린드롬이 홀수(중간에 짝이 없는 값이 있음) ex. "abcba"
        while i-j >= 0 and i+j < N:
            if s[i-j] == s[i+j]:    
                mid_o += 2
                j += 1
            else:
                break
        answer = max(mid_o,answer)
        
        k = 0
        mid_x = 0
        # 팰린드롬이 짝수(모든 수가 짝이 있음) ex. "baab"
        while i-k >= 0 and i+k+1 < N:
            if s[i-k] == s[i+k+1]:
                mid_x += 2
                k += 1
            else:
                break
        answer = max(mid_x,answer)
        
    return answer