def solution(s):
    answer = [0,0]
    # s가 1이 될때까지
    while s != "1":
        answer[0] += 1
        zero,one = 0,0
        # 0,1의 개수 카운팅
        for bit in s:
            if bit == "1":
                one += 1
            else:
                zero += 1
        answer[1] += zero
        s_next = ""
        if one == 1:    # 1이 한개면 break
            break
        # 이진화
        while one > 1:
            share,rem = divmod(one,2)
            s_next += str(rem)
            one = share
            if share == 1:
                s_next += str(share)
                break
                
        s = s_next[::-1]
            
    return answer