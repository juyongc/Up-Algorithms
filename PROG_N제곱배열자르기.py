def solution(n, left, right):
    answer = [0]*(right-left+1)
    x1,y1 = divmod(left,n)
    x2,y2 = divmod(right,n)
    cnt = 0
    
    # left ~ right까지 몫,나머지 구하기
    # 해당 위치 값은 max(몫,나머지)+1
    for num in range(left,right+1):
        share,rem = divmod(num,n)
        answer[cnt] = max(share,rem)+1
        cnt += 1

    return answer