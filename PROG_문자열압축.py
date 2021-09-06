def solution(s):
    answer = 0
    short = len(s)
    maxi = len(s) // 2
    # 문자열 자를 숫자 정하기(max = 문자열 // 2)
    for i in range(1,maxi+1):
        ns = ''
        now = i
        prev = s[0:i]
        cnt = 1
        # 다음 자를 문자열 인덱스가 전체 문자열보다 커질때까지 자르기
        while now+i <= len(s):
            cur = s[now:now+i]
            if prev == cur:
                cnt += 1
            else:
                if cnt == 1:
                    ns += prev
                else:
                    ns += (str(cnt) + prev) 
                cnt = 1
            prev = cur[:]
            now = now+i
            
        if cnt != 1:    # 1보다 크면 숫자 string 변환 후 더하기
            ns += str(cnt)
        ns += prev      # 이전에 자른 문자열 더하기
        if now < len(s):    # 남은 문자열 더해주기
            ns += s[now:len(s)]
        if len(ns) > 0 and len(ns) < short: # 길이 비교
            short = len(ns)
    return short