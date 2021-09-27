def solution(n):
    answer = ''
    rules = [1,2,4]
    pos = n
    num = 1
    # 자릿수 찾기
    while pos > 0:
        if pos - (3**num) > 0:
            pos -= (3**num)
            num += 1
        else:
            break
    
    now = [1]*num
    val = num
    # 나머지가 0일때까지 구하기
    if pos > 0:
        for i in range(num,0,-1):
            for j in range(3):
                if pos - 3**(i-1) < 0:
                    now[num-i] = rules[j]
                    break
                elif pos - 3**(i-1) == 0:
                    now[num-i] = rules[j]
                    if i == 1:
                        pos -= 3**(i-1)
                    break
                else:
                    pos -= 3**(i-1)
                
            if pos == 0:
                break
        
    answer = ''.join(map(str,now))
            
    return answer