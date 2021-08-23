def solution(brown, yellow):
    # 2(w+h)+4 = brown
    # w*h = yellow
    summ=(brown-4)//2
    # 1 ~ summ-1 중에서 조건 만족 값 찾기
    for w in range(1,summ):
        h = summ - w
        if w*h == yellow:
            break
    answer = [h+2,w+2]  # 가로 >= 세로
    return answer