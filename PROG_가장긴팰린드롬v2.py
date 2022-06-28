def solution(s):
    answer = 1
    
    for i in range(len(s)-1):
        cnt = 1
        # 현재 위치 값이 뒤에 값과 같으면 짝수 팬린드롬 체크
        if s[i] == s[i+1]:
            l,r = i-1,i+2
            cnt += 1
            
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    cnt += 2
                else:
                    break
                l -= 1
                r += 1
        
            answer = max(answer,cnt)
        # 현재 위치 값을 기준으로 앞,뒤로 팬림드롬 체크
        cnt = 1    
        l,r = i-1,i+1
        
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                cnt += 2
            else:
                break
            l -= 1
            r += 1
        
            answer = max(answer,cnt)
        

    return answer