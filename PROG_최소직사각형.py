def solution(sizes):
    answer = 0
    num = len(sizes)
    maxi = 0
    mini = 0
    # 가/세로 중에서 큰값,작은값 찾아서
    # 각각 maxi,mini랑 비교 후 갱신
    for size in sizes:
        a,b = size[0],size[1]
        if a >= b:
            if a > maxi:
                maxi = a
            if b > mini:
                mini = b
        else:
            if b > maxi:
                maxi = b
            if a > mini:
                mini = a
    answer = maxi * mini
    return answer