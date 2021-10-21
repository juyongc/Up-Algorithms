def solution(arr):
    now = arr[0]
    # 리스트 안 모든 숫자 확인
    for num in arr:
        # 최소값 찾기
        if now >= num:
            s = num
        else:
            s = now
        # 가장 큰 수부터 내려오면서 둘 다 나머지 = 0 값 찾기
        for s in range(num,0,-1):
            cnow = now % s
            cnum = num % s
            if cnow == 0 and cnum == 0:
                now *= (num // s)
                break
    answer = now
    return answer